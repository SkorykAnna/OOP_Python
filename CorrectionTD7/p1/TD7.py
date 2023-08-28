import praw
import pandas as pd
from collections import defaultdict
from Document import Document
from Author import Author
from Corpus import Corpus

# PRAW Reddit instance
reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw', client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ', user_agent='bocca')

# Retrieve posts from the logistics subreddit
posts = []
log_subreddit = reddit.subreddit('all') #if you want to find some specific them, please make sure that it's not limited
for post in log_subreddit.hot(limit=300): #limit is the number of posts you want to check and wright it down
    posts.append([post.id, post.author, post.title, post.url, post.num_comments, post.selftext, post.subreddit])
posts = pd.DataFrame(posts, columns=['id', 'author', 'title', 'url', 'num_comments', 'body', 'subreddit'])

keyword = '3pl'
limit = 3

#post[0] post id
#post[1] author
#post[2] title
#post[3] url
#post[4] num_comments
#post[5] body
#post[6] subreddit

# Retrieve self-text from submissions with the given keyword
texts = []
for submission in log_subreddit.search(keyword, limit=limit):
    text = submission.selftext.replace('\n', ' ')
    texts.append(text)

corpus = Corpus()
num_posts = 3  # Number of posts to print

# Add documents to the corpus
for post_number, post in enumerate(posts.itertuples(index=False), start=1):
    #self, body, title, id, subreddit, url, num_comments, author
    author = Author(post[1])  # Create an Author object
    doc = Document(post[5], post[2], post[0], post[6], post[3], post[4], author)  # Pass the author object to the Document
    doc.post_number = post_number
    corpus.add_document(doc)


corpus.build_vocab()
corpus.compute_tf_matrix()
corpus.compute_tfidf_matrix()

# Print information about each document in the corpus
for i, doc in enumerate(corpus.documents[:num_posts]):
    print("Post Number:", doc.post_number)  # Print the post number
    print("Document ID:", doc.id)
    print("Author:", doc.author.name)
    print("Score:", doc.title)
    print("Subreddit:", doc.subreddit)
    print("URL:", doc.url)
    print("Number of Comments:", doc.num_comments)
    print("Body:", doc.body)
    print()

# Access the matTF matrix
print("TF Matrix:")
print(corpus.matTF.toarray())
print()

# Access the matTFxIDF matrix
print("TF-IDF Matrix:")
print(corpus.matTFxIDF.toarray())
