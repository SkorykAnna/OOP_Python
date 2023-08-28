#1.1 The task involves implementing a "search" function in the Corpus class that returns passages containing the entered keyword, 
    ##working with a concatenated string of document texts.
    #let's check it by using regular expressions to search for specific keywords

from Corpus import Corpus
import pandas as pd
import generate_docs


# Access the DataFrame from generate_docs.py
df = generate_docs.df
df.to_csv('output.csv', sep='\t', index=False)

# Read the CSV file generated in "generate_doc"
df = pd.read_csv('output.csv', sep='\t')

# Get the 'Text' column from the DataFrame
texts = df['Text'].tolist()
corpus = Corpus()
corpus.add_document(df['Text'].str.cat(sep=' '))

result = corpus.search("broker")
print(result)


