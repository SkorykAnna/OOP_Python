import re
from collections import Counter

class Document:
    def __init__(self, body, author, post_id, url, num_comments, title):
        self.body = str(body)  # Convert body to string
        self.author = author
        self.post_id = post_id
        self.url = url
        self.num_comments = num_comments
        self.title = title
        self.words = self.extract_words(body)  # Extract words from the body text

    def extract_words(self, text):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        words = re.split(delimiters, text)
        return words
        

    
    def get_tf_vector(self, vocabulary):
        tf_vector = {word: 0 for word in vocabulary}
        word_counts = Counter(self.words)
        total_words = len(self.words)
        
        for word, count in word_counts.items():
            tf_vector[word] = count / total_words
        
        return tf_vector

