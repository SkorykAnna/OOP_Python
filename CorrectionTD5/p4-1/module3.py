#4.1
    # To implement the Singleton pattern in Python, need to modify the Corpus class to ensure that only one instance of the class can be created
from Corpus import Corpus
from Document import RedditDocument, ArxivDocument
import praw
import urllib.request
import xmltodict


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


def get_arxiv_texts():
    base_url = 'http://export.arxiv.org/api/query'
    search_query = 'cat:cs.AI'
    results_per_page = 10

    query_url = f'{base_url}?search_query={search_query}&max_results={results_per_page}'

    response = urllib.request.urlopen(query_url)
    data = response.read()

    parsed_data = xmltodict.parse(data)

    texts = []

    for entry in parsed_data['feed']['entry']:
        text = entry['summary']
        texts.append(text)

    return texts


corpus1 = Corpus("Corpus 1")
corpus2 = Corpus("Corpus 2")

# Get texts from Reddit API
reddit_texts = get_reddit_texts()

    # Add Reddit documents to the corpus
for text in reddit_texts:
    reddit_doc = RedditDocument("3PL", "Europe", "2022-06-01", "https://reddit.com", text, 10)
    corpus1.add_document(1, reddit_doc)

    # Get texts from Arxiv API
arxiv_texts = get_arxiv_texts()

    # Add Arxiv documents to the corpus
for text in arxiv_texts:
    arxiv_doc = ArxivDocument("Logistics", ["USA", "Canada"], "2022-06-02", "https://arxiv.org", text)
    corpus2.add_document(2, arxiv_doc)

    
print(corpus1)
print()
print(corpus2)
print()
print(corpus1 is corpus2)  # True, both variables refer to the same instance