import pandas as pd
import math
from collections import defaultdict
from scipy.sparse import csr_matrix

class Corpus:
    def __init__(self):
        self.documents = []
        self.vocab = {}
        self.matTF = None
        self.matTFxIDF = None

    def add_document(self, document):
        self.documents.append(document)

    def build_vocab(self):
        words = []
        for doc in self.documents:
            text = doc.get_text()
            doc_words = text.lower().split()
            words.extend(doc_words)

        words = list(set(words))
        words.sort()

        for i, word in enumerate(words):
            self.vocab[word] = {'id': i, 'total_occurrences': 0, 'doc_frequency': 0}

    def compute_tf_matrix(self):
        num_docs = len(self.documents)
        num_words = len(self.vocab)
        matrix_data = []
        row_indices = []
        col_indices = []

        for i, doc in enumerate(self.documents):
            text = doc.get_text()
            words = text.lower().split()
            word_counts = defaultdict(int)
            for word in words:
                if word in self.vocab:
                    word_id = self.vocab[word]['id']
                    word_counts[word_id] += 1
                    self.vocab[word]['total_occurrences'] += 1

            if word_counts:  # Check if word_counts is not empty
                max_word_count = max(word_counts.values())
            else:
                max_word_count = 0

            for word_id, count in word_counts.items():
                tf = count / max_word_count
                matrix_data.append(tf)
                row_indices.append(i)
                col_indices.append(word_id)

        self.matTF = csr_matrix((matrix_data, (row_indices, col_indices)), shape=(num_docs, num_words))


    def compute_tfidf_matrix(self):
        num_docs = len(self.documents)
        num_words = len(self.vocab)
        matrix_data = []
        row_indices = []
        col_indices = []

        for i, doc in enumerate(self.documents):
            text = doc.get_text()
            words = text.lower().split()
            word_counts = defaultdict(int)
            for word in words:
                if word in self.vocab:
                    word_id = self.vocab[word]['id']
                    word_counts[word_id] += 1

            if word_counts:  # Check if word_counts is not empty
                max_word_count = max(word_counts.values())
            else:
                max_word_count = 0

            for word_id, count in word_counts.items():
                tf = count / max_word_count
                if word_id in self.vocab:
                    idf = math.log(num_docs / self.vocab[word_id]['doc_frequency'])
                    tfidf = tf * idf
                    matrix_data.append(tfidf)
                    row_indices.append(i)
                    col_indices.append(word_id)

        self.matTFxIDF = csr_matrix((matrix_data, (row_indices, col_indices)), shape=(num_docs, num_words))

