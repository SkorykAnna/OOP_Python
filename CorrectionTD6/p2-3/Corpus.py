import re
import pandas as pd
from collections import Counter

class Corpus:
    def __init__(self, texts):
        self.texts = texts
        self.vocabulary = set()
    
    def build_vocabulary(self):
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        
        for text in self.texts:
            words = re.split(delimiters, text)
            self.vocabulary.update(words)
    
    def count_word_occurrences(self):
        word_counts = Counter()
        
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        
        for text in self.texts:
            words = re.split(delimiters, text)
            word_counts.update(words)
        
        return word_counts

    def create_word_frequency_dataframe(self):
        word_counts = self.count_word_occurrences()
        df = pd.DataFrame({'Word': list(word_counts.keys()), 'Frequency': list(word_counts.values())})
        return df