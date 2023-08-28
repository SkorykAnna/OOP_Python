#3.4
    # Import the required modules
from Document import Document
from Corpus import Corpus
from datetime import datetime

    # Create a test corpus with authors and documents
        # Function to retrieve texts from Reddit API
def get_reddit_texts(keyword, limit=10):
        import praw

        reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw',
                             client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ',
                             user_agent='bocca')
        subreddit = reddit.subreddit('all')

        texts = []

        for submission in subreddit.search(keyword, limit=limit):
            text = submission.selftext.replace('\n', ' ')
            texts.append(text)

        return texts    
# Example usage
texts = get_reddit_texts("example keyword", limit=10)
corpus = Corpus("Reddit Corpus")
for i, text in enumerate(texts):
    doc = Document(f"Document {i+1}", "Reddit User", datetime.now().date(), "www.example.com", text)
    corpus.add_document(i+1, doc)

corpus.sort_documents_by_date()
corpus.sort_documents_by_title()