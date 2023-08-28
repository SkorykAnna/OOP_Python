import re

class Corpus:
    def __init__(self, texts):
        self.texts = texts
        self.vocabulary = set()
    
    def build_vocabulary(self):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        
        for text in self.texts:
            words = re.split(delimiters, text)
            self.vocabulary.update(words)
    
    def get_vocabulary(self):
        return self.vocabulary