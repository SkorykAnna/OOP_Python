#2.2
    #Updating Author.py file with this code:
#class Author:
#    def __init__(self, name):
#        self.name = name
 #       self.ndoc = 0
#        self.production = {}

#    def add_document(self, doc_id, document):
#        self.production[doc_id] = document
#        self.ndoc += 1

 #   def __str__(self):
#        return f"Author: {self.name}\nNumber of Documents: {self.ndoc}"


        #Using our .py files that was created
        # Importing the necessary modules
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

# Retrieve the texts from Reddit API
texts = get_reddit_texts()

# Create an instance of Author
author1 = Author("Mariusz Kmiecik")

# Create instances of Document using the texts from Reddit API
for i, text in enumerate(texts, start=1):
    doc = Document(f"Reddit Document {i}", "Unknown", datetime.now().date(), "", text)
    author1.add_document(i, doc)

# Print the author information
print(author1)