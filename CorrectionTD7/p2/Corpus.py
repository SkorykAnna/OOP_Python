import re
import numpy as np
from collections import defaultdict


class Corpus:
    def __init__(self, texts):
        self.texts = texts
        self.vocabulary = set()
        self.documents = []
        self.word_to_index = {}  # New attribute for word-to-index mapping
    
    def add_document(self, document):
        self.documents.append(document)

    def build_vocabulary(self):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        
        for document in self.documents:
            words = re.split(delimiters, document.body)
            self.vocabulary.update(words)
        
        self.word_to_index = {word: index for index, word in enumerate(self.vocabulary)}
       
    def compute_tfidf_matrix(self):
        self.tfidf_matrix = np.zeros((len(self.documents), len(self.vocabulary)))

        for i, document in enumerate(self.documents):
            tf_vector = dict(document.get_tf_vector(self.vocabulary))
            idf_vector = self.get_idf_vector()

            for word in tf_vector:
                self.tfidf_matrix[i, self.word_to_index[word]] = tf_vector[word] * idf_vector[word]

        return self.tfidf_matrix


    def get_idf_vector(self):
        idf_vector = defaultdict(int)
        num_documents = len(self.documents)
        
        for document in self.documents:
            for word in document.words:
                idf_vector[word] += 1
        
        for word, frequency in idf_vector.items():
            idf_vector[word] = np.log(num_documents / frequency)
        
        return idf_vector
    
    def search(self, query, num_results=5):
        query_vector = self.get_query_vector(query)
        scores = np.dot(self.tfidf_matrix, query_vector)
        top_indices = np.argsort(scores)[::-1][:num_results]
        
        similarity_scores = [(index, scores[index]) for index in top_indices]
        
        for doc_index, similarity in similarity_scores:
            document = self.documents[doc_index]
            num_matching_words = self.get_num_matching_words(document.words, query)
            if num_matching_words > 0:
                print("Title:", document.title)
                print("Author:", document.author)
                print("URL:", document.url)
                print("Similarity Score:", similarity)
                print("Number of Matching Words:", num_matching_words)
                print("----------------------------------")
            else:
                print("No match found")

    
    def get_query_vector(self, query):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        words = re.split(delimiters, query)
        query_vector = [words.count(word) for word in self.vocabulary]
        return np.array(query_vector)
    
    def get_num_matching_words(self, document_words, query):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        query_words = re.split(delimiters, query)
        matching_words = set(document_words) & set(query_words)
        return len(matching_words)
