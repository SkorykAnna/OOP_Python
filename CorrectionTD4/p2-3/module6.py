#2.3
        # creating the id2aut dictionary containing authors with their names as unique keys
import praw
from Author import Author
from Document import Document
from datetime import datetime

# Function to retrieve texts from Reddit API
def get_reddit_texts():
    reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw',
                         client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ',
                         user_agent='bocca')
    subreddit = reddit.subreddit('all')
    keyword = '3pl'
    limit = 10

    texts = []

    for submission in subreddit.search(keyword, limit=limit):
        text = submission.selftext.replace('\n', ' ')
        texts.append(text)

    return texts

# Create dictionaries to store the Document instances and Author instances
id2doc = {}
id2aut = {}

# Function to add a document to the dictionaries
def add_document(doc_id, doc):
    # Check if the author is known
    if doc.auteur not in id2aut:
        # Create a new Author instance
        author = Author(doc.auteur)
        # Add the Author instance to the id2aut dictionary
        id2aut[doc.auteur] = author
    # Add the Document instance to the id2doc dictionary
    id2doc[doc_id] = doc
    # Get the author associated with the document
    author = id2aut[doc.auteur]
    # Add the document to the author's production
    author.add_document(doc_id, doc)

# Retrieve the texts from Reddit API
texts = get_reddit_texts()

# Create Document instances using the texts from Reddit API and add them to the dictionaries
for i, text in enumerate(texts, start=1):
    doc = Document(f"Reddit Document {i}", "Unknown", datetime.now().date(), "", text)
    add_document(i, doc)

# Print the information of each document
for doc_id, doc in id2doc.items():
    print(f"Document ID: {doc_id}")
    doc.display_info()
    print()

# Print the authors and their associated documents
for author_name, author in id2aut.items():
    print(author)
    print()

# Print the size of the corpus
corpus_size = len(id2doc)
print(f"Corpus size: {corpus_size}")
