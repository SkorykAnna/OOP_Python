import re
from collections import Counter
import pandas as pd

class Corpus:
    def __init__(self, texts):
        self.texts = texts
    
    def clean_text(self, text):
        text = text.lower()  # Convert text to lowercase
        text = re.sub(r'\n', ' ', text)  # Replace newline characters with spaces
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\d+', '', text)  # Remove numbers
        return text
    
    def stats(self, n):
        cleaned_texts = [self.clean_text(text) for text in self.texts]
        all_words = ' '.join(cleaned_texts).split()
        
        unique_words_count = len(set(all_words))
        print("Number of unique words in the corpus:", unique_words_count)
        
        word_frequencies = Counter(all_words)
        top_n_words = word_frequencies.most_common(n)
        print("Top", n, "most frequent words:")
        for word, frequency in top_n_words:
            print(word, "-", frequency)