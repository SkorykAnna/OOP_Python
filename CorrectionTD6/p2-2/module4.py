 #2.2
    #The code defines a Corpus class that builds a vocabulary by splitting texts using specific delimiters and stores the unique words in a set.

from Corpus import Corpus
import pandas as pd
import generate_docs

# Access the DataFrame from generate_docs.py
df = generate_docs.df
df['Text'] = df['Text'].fillna('')  # Replace NaN values with empty strings
df.to_csv('output.csv', sep='\t', index=False)

# Read the CSV file generated in "generate_doc"
df = pd.read_csv('output.csv', sep='\t')

# Get the 'Text' column from the DataFrame
texts = df['Text'].fillna('').astype(str).tolist()  # Replace NaN values with empty strings and convert to strings

# Create an instance of the Corpus class
corpus = Corpus(texts)

# Build the vocabulary
corpus.build_vocabulary()

# Get the vocabulary
vocabulary = corpus.get_vocabulary()

print(vocabulary)