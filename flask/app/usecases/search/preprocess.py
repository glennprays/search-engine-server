import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
from num2words import num2words


class Preprocess:
    def convert_lower_case(self, doc):
        return np.char.lower(np.array(doc, dtype=np.str_))

    def stop_word_filtering(self, doc):
        stop_words = set(stopwords.words("english"))
        return [word for word in doc if word not in stop_words]

    def remove_punctuation(self, doc):
        translation_table = str.maketrans("", "", string.punctuation)
        return [
            word.translate(translation_table)
            for word in doc
            if word.translate(translation_table) != ""
        ]

    def remove_non_printable_from_words(self, doc):
        def remove_non_printable(word):
            return "".join(char for char in word if char in string.printable)

        return [remove_non_printable(word) for word in doc]

    def remove_apostrophe(self, doc):
        return [word.replace("'", "") for word in doc]

    def remove_single_char(self, doc):
        return [word for word in doc if len(word) > 1]

    def word_stemming(self, doc):
        porter_stemmer = PorterStemmer()
        return [porter_stemmer.stem(word) for word in doc]

    def get_wordnet_pos(self, word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV,
            "J": wordnet.ADJ,
        }
        return tag_dict.get(tag, wordnet.NOUN)

    def word_lemmatization(self, doc):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(word)) for word in doc]
    
    def is_string_number(self, s):
        try:
            int_value = int(s)
            return True
        except ValueError:
            return False
        
    def number_to_word(self, num):
        words = num2words(num)
        token = nltk.word_tokenize(words)
        doc = self.convert_lower_case(token)
        return doc

    def convert_number(self, doc):
        result = []
        for word in doc:
            if self.is_string_number(word):
                result.extend(self.number_to_word(word))
            else:
                result.append(word)
        return result
    
    def preprocess(self, doc):
        doc = self.convert_number(doc)
        doc = self.convert_lower_case(doc)
        doc = self.stop_word_filtering(doc)
        doc = self.remove_non_printable_from_words(doc)
        doc = self.remove_punctuation(doc)
        doc = self.remove_apostrophe(doc)
        doc = self.remove_single_char(doc)
        doc = self.word_lemmatization(doc)
        doc = self.word_stemming(doc)

        return doc