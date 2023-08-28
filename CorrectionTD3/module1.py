# Partie 1 
    
    #1.1 Reddit
import praw  #need to instal pip install praw

reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw', client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ', user_agent='bocca')

hot_posts = reddit.subreddit('all').hot(limit=10)
    #list of 10 titles
print("List of 10 titles")
for post in hot_posts:
    print(post.title)
print()

    #Quels sont les champs disponibles ?
    # the list of attributes that can be used with post
print("The list of attributes that can be used with post: ")
for post in hot_posts:
    print(dir(post))
print()

    #Quel est le champ contenant le contenu textuel ?
    #The field that contains the content text. This will allow you to retrieve the text contained within the post.
print("The field that contains the content text: ")
for post in hot_posts:
    print(post.selftext)
print()

    #Print the textual content of each post, removing newlines (\n)
print("The textual content of each post, removing newlines: ")
for post in hot_posts:
    text = post.selftext.replace('\n', ' ')
    print(text)
print()

    #generating information (data) with using list of fields
print("Generated info (subreddit 'logistics') with using list of fields: ")
import pandas as pd
posts = []
log_subreddit = reddit.subreddit('logistics')
for post in log_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
print()

    # General information about the subreddit 
print("General information about the subreddit 'logistics': ")
log_subreddit = reddit.subreddit('logistics')
print(log_subreddit.description)
print()

    #Get comments from a specific post
submission = reddit.submission(url="https://new.reddit.com/r/FreightBrokers/comments/12czhzb/more_like_dude_who_has_my_load/")

    #  get the top-level comments 
print("The top-level comments: ")
for top_level_comment in submission.comments:
    print(top_level_comment.body)
print()

    # get rid of the MoreComments objects
print("The top-level comments without the MoreComments objects: ")
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)
print()

    #same thing, another method
print("The top-level comments without the MoreComments objects (another method): ")
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
print()

    #Print the textual content of each post, removing newlines (\n)
print("The textual content of each post, removing newlines: ")
for top_level_comment in submission.comments:
   text = top_level_comment.body.replace('\n', ' ')
   print(text)
print()