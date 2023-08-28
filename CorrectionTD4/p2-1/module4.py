#2.1
    # Was created .py document that we have in same folder/directory ("Author.py" file) wich includes:
#class Author:
#    def __init__(self, name):
#        self.name = name
#        self.ndoc = 0
 #       self.production = {}

#    def add_document(self, doc_id, document):
#        self.ndoc += 1
#        self.production[doc_id] = document

#    def get_document_ids(self):
#        return list(self.production.keys())

    #Using our .py files that was created
    # Importing the necessary modules
import praw
from datetime import datetime
from Document import Document
from Author import Author

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

# Retrieve the texts from Reddit API
texts = get_reddit_texts()

# Create an instance of Author
author1 = Author("clic")

# Create instances of Document using the texts from Reddit API
for i, text in enumerate(texts, start=1):
    doc = Document(f"Reddit Document {i}", "Unknown", datetime.now().date(), "", text)
    author1.add_document(i, doc)

# Get the document IDs associated with the author
document_ids = author1.get_document_ids()

# Print the document IDs
print(f"Document IDs associated with {author1.name}: {document_ids}")

