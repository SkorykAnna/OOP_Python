#2.3
    #This code uses the Counter class from the collections module to efficiently count word occurrences while iterating over the texts only once.

        #The resulting word frequency DataFrame is providing the desired output.

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

# Create the word frequency DataFrame
df = corpus.create_word_frequency_dataframe()

print(df)