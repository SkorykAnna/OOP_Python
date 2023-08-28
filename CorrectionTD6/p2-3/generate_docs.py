import praw
import pandas as pd
import urllib.request
import xmltodict

def get_reddit_texts():
    reddit = praw.Reddit(client_id='wB9k5Cv_5f8Ujr9gDBHXsw',
                         client_secret='eXgC7RQcXvL8nic6bYV2gs4_RewbhQ',
                         user_agent='bocca')
    subreddit = reddit.subreddit('logistics')

    texts = []

    for submission in subreddit.new():  # Retrieve the latest submissions
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

reddit_texts = get_reddit_texts()
arxiv_texts = get_arxiv_texts()
all_texts = reddit_texts + arxiv_texts

df = pd.DataFrame({'Text': all_texts, 'Origin': ['Reddit'] * len(reddit_texts) + ['Arxiv'] * len(arxiv_texts)})
df['ID'] = range(1, len(df) + 1)


# Return the DataFrame at the end
df
