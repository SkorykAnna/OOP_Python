 #2.1
    #The given code defines a Corpus class that performs text processing operations such as cleaning, 
    #and provides a stats() method to display the number of unique words in the corpus and the top n most frequent words
    #checking code with using the stats() method to display the desired statistics
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

# Use the stats method to display statistics
corpus.stats(5)