#1.2 The concordance function in the Corpus class retrieves and stores occurrences of a given expression along with their left and right contexts in a pandas DataFrame.
#the output includes the left context, match, and right context for each occurrence of the expression
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
texts = df['Text'].astype(str).tolist()  # Convert all values to strings

# Create an instance of the Corpus class
corpus = Corpus(texts)

# Use the concorde method to generate the concordance DataFrame
concordance_df = corpus.concorde("is", 10)

# Print the concordance DataFrame
print(concordance_df)


