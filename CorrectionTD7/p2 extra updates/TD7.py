import pandas as pd
import praw
import prawcore
from Document import Document
from Corpus import Corpus
from Author import Author


# PRAW Reddit instance
reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw', client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ', user_agent='bocca')

# Retrieve posts from the logistics subreddit
posts = []
sub = input("Enter a search subreddit (all, logistics, computerscience as example): ")
count = input("Enter a count of posts to search: ")
print("Loading...")
print()
try:
    log_subreddit = reddit.subreddit(sub)  # If the subreddit doesn't exist, prawcore.exceptions.Redirect will be raised
    for post in log_subreddit.hot(limit=int(count)):
        posts.append([post.id, post.author, post.title, post.url, post.num_comments, post.selftext])
    posts = pd.DataFrame(posts, columns=['id', 'author', 'title', 'url', 'num_comments', 'body'])


#post[0] post id
#post[1] author
#post[2] title
#post[3] url
#post[4] num_comments
#post[5] body

    # Create a Corpus object
    texts = [post for post in posts]
    corpus = Corpus(texts)

    # Add documents to the corpus
    for post_number, post in enumerate(posts.itertuples(index=False), start=1):
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
    
except prawcore.exceptions.Redirect:
    print("No such subreddit was found.")