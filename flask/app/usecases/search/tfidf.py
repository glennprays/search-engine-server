import math

class TFIDFCalculator:
    def calculate_tf(self, docs):
        tf = []
        for doc in docs:
            doc_tf = {}
            for word in doc:
                doc_tf[word] = doc_tf.get(word, 0) + 1 
            tf.append(doc_tf)
        return tf

    def calculate_idf(self, docs):
        idf = {}
        total_documents = len(docs)

        for doc in docs:
            unique_words = set(doc)
            for word in unique_words:
                idf[word] = idf.get(word, 0) + 1

        for word, count in idf.items():
            idf[word] = math.log10(total_documents / count)

        return idf

    def calculate_tfidf(self, docs, tf, idf):
        tfidf = []
        for i, doc in enumerate(docs):
            doc_tfidf = {}
            for word in doc:
                doc_tfidf[word] = tf[i][word] * idf.get(word, 0)  
            tfidf.append(doc_tfidf)
        return tfidf