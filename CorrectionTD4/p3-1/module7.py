#3.1
        # Was created .py document that we have in same folder/directory ("Corpus.py" file)

    # Using these files
from Corpus import Corpus, get_reddit_texts

# Create an instance of Corpus
corpus = Corpus("My Corpus")

# Retrieve the texts from Reddit API
texts = get_reddit_texts()

# Add documents to the corpus
for i, doc in enumerate(texts, start=1):
    corpus.add_document(i, doc)

# Print the information of each document
for doc_id, doc in corpus.id2doc.items():
    print(f"Document ID: {doc_id}")
    doc.display_info()
    print()

# Print the authors and their associated documents
for author_name, author in corpus.authors.items():
    print(author)
    print()

# Print the size of the corpus
print(corpus)
