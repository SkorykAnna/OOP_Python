from Author import Author
from Document import Document
import praw


class Corpus:
    def __init__(self, name):
        self.nom = name
        self.authors = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

    def add_document(self, doc_id, doc):
        # Check if the author is known
        if doc.auteur not in self.authors:
            # Create a new Author instance
            author = Author(doc.auteur)
            # Add the Author instance to the authors dictionary
            self.authors[doc.auteur] = author
            self.naut += 1
        else:
            author = self.authors[doc.auteur]
        # Add the Document instance to the id2doc dictionary
        self.id2doc[doc_id] = doc
        self.ndoc += 1
        # Add the document to the author's production
        author.add_document(doc_id, doc)

def get_reddit_texts():
    reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw',
                         client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ',
                         user_agent='bocca')
    subreddit = reddit.subreddit('all')
    keyword = '3pl'
    limit = 10

    texts = []

    for submission in subreddit.search(keyword, limit=limit):
        title = submission.title
        author = submission.author.name if submission.author else "Unknown"
        date = submission.created_utc
        url = submission.url
        text = submission.selftext.replace('\n', ' ')

        doc = Document(title, author, date, url, text)
        texts.append(doc)

    return texts
