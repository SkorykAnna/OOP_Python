import re
import pandas as pd

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
        word_counts = {word: 0 for word in self.vocabulary}
        document_frequency = {word: 0 for word in self.vocabulary}  # New dictionary for document frequency
        
        delimiters = r'\s+|[.,!?;:"]'  # Delimiters for splitting the text
        
        for text in self.texts:
            words = re.split(delimiters, text)
            unique_words = set(words)  # Unique words in the current text
            
            for word in unique_words:
                if word in self.vocabulary:
                    word_counts[word] += words.count(word)
                    document_frequency[word] += 1
        
        df = pd.DataFrame({'Word': list(word_counts.keys()), 'Frequency': list(word_counts.values()), 'Document Frequency': list(document_frequency.values())})
        return df