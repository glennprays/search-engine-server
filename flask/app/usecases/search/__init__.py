from flask import jsonify
import math
import nltk
from .preprocess import Preprocess
from .json_file import JsonFileManager
from .tfidf import TFIDFCalculator
from urllib.parse import quote
import os


preprocess = Preprocess()
json_file = JsonFileManager()
tfidf = TFIDFCalculator()


docs_preprocessed = json_file.load_json("./tfidf/docs_preprocessed.json")
docs_list = json_file.load_json("./tfidf/docs_list.json")
docs_tf = json_file.load_json("./tfidf/docs_tf.json")
docs_idf = json_file.load_json("./tfidf/docs_idf.json")
docs_tfidf = json_file.load_json("./tfidf/docs_tfidf.json")

class SearchUseCase:
    def search_query(self, query):
        preprocessed_query = preprocess.preprocess(nltk.word_tokenize(query))

        query_tfidf = tfidf.calculate_tfidf([preprocessed_query], tfidf.calculate_tf([preprocessed_query]), docs_idf)[0]

        result = self.find_matching_documents(query_tfidf, docs_tfidf)
        result = [tupel for tupel in result if tupel[1] > 0.0999]
        documents = []
        for tupel in result:
            if tupel[1] > 0.0999:
                filename = docs_list[tupel[0]]
                filepath = os.path.join('./documents/',filename)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                    snippet = file.read(150)

                temp = {
                    "snippet": snippet,
                    "filename": filename,
                    "url": quote("/api/documents/"+filename),
                    "consine_similarity": tupel[1]
                }
                documents.append(temp)

        return jsonify({"query": query, "documents": documents}), 200
    
    def cosine_similarity(self, query_tfidf, doc_tfidf):
        dot_product = sum(query_tfidf.get(word, 0) * doc_tfidf.get(word, 0) for word in set(query_tfidf) & set(doc_tfidf))
        query_norm = math.sqrt(sum(value**2 for value in query_tfidf.values()))
        document_norm = math.sqrt(sum(value**2 for value in doc_tfidf.values()))
        
        if query_norm == 0 or document_norm == 0:
            return 0
        
        similarity = dot_product / (query_norm * document_norm)
        return similarity
    
    def find_matching_documents(self, query_tfidf, documents_tfidf):
        similarities = [self.cosine_similarity(query_tfidf, doc_tfidf) for doc_tfidf in documents_tfidf]
        
        matching_documents = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
        return matching_documents