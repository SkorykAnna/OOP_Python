#3.3
    #Updating our file Corpus.py


        # Using these files
from Corpus import Corpus

corpus = Corpus("My Corpus")

# Add documents to the corpus from Reddit
corpus.get_reddit_documents("python", limit=5)

# Save the corpus to a file
corpus.save("corpus.csv")

# Load the corpus from the file
loaded_corpus = Corpus.load("corpus.csv")

# Sort and display documents by date from the loaded corpus
print("Sorted Documents by Date (Loaded Corpus):")
loaded_corpus.sort_documents_by_date()

# Sort and display documents by title from the loaded corpus
print("Sorted Documents by Title (Loaded Corpus):")
loaded_corpus.sort_documents_by_title()

# Print the loaded corpus representation
print(repr(loaded_corpus))


