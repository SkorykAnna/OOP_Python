import pandas as pd
import praw
from Document import Document
from Corpus import Corpus
from Author import Author


# PRAW Reddit instance
reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw', client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ', user_agent='bocca')

# Retrieve posts from the logistics subreddit
posts = []
log_subreddit = reddit.subreddit('all') #if you want to find some specific them, please make sure that it's not limited
for post in log_subreddit.hot(limit=300): #limit is the number of posts you want to check and wright it down
    posts.append([post.id, post.author, post.title, post.url, post.num_comments, post.selftext])
posts = pd.DataFrame(posts, columns=['id', 'author', 'title', 'url', 'num_comments', 'body'])

#post[0] post id
#post[1] author
#post[2] title
#post[3] url
#post[4] num_comments
#post[5] body

# Create a Corpus object
texts = [post for post in posts]  # Assuming 'posts' is a list of strings representing the body text
corpus = Corpus(texts)


# Add documents to the corpus
for post_number, post in enumerate(posts.itertuples(index=False), start=1):
    #self, body, author, post_id, url, num_comments, title
    author = Author(post[1])  # Create an Author object
    doc = Document(post[5], author, post[0], post[3], post[5], post[2])
    doc.post_number = post_number
    corpus.add_document(doc)

corpus.build_vocabulary()
corpus.compute_tfidf_matrix()

# Perform search
print("You are looking in subreddit: " + str(log_subreddit))
query = input("Enter a search query: ")
corpus.search(query)