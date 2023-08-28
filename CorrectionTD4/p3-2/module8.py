#3.2
        #Updating file Corpus.py

        # Using these files
from Corpus import Corpus, get_reddit_documents

# Create an instance of Corpus
corpus = Corpus("My Corpus")

# Retrieve the documents from Reddit API
documents = get_reddit_documents()

# Add documents to the corpus
for i, doc in enumerate(documents, start=1):
    corpus.add_document(i, doc)

# Sort and display documents by date
print("Sorted Documents by Date:")
corpus.sort_documents_by_date()

# Sort and display documents by title
print("Sorted Documents by Title:")
corpus.sort_documents_by_title()

# Print the corpus representation
print(repr(corpus))