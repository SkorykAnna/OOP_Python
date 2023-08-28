import praw  #need to instal pip install praw
import pandas as pd
import urllib.request
    # the removal of links using the re module
import re
    # To parse the results using the xmltodict library, you can convert the XML response data into a Python dictionary using the xmltodict.parse() function. 
import xmltodict #need instal pip install xmltodict

#Partie 2

    #2.1
    #using from ex 1.1  info and ex 1.2 

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

    # Function to retrieve texts from Arxiv API
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

    # Get texts from Reddit API
reddit_texts = get_reddit_texts()

    # Get texts from Arxiv API
arxiv_texts = get_arxiv_texts()

    # Combine texts from both APIs
all_texts = reddit_texts + arxiv_texts

    # Create DataFrame
df = pd.DataFrame({'Text': all_texts, 'Origin': ['Reddit'] * len(reddit_texts) + ['Arxiv'] * len(arxiv_texts)})

    # Add unique IDs to the DataFrame
df['ID'] = range(1, len(df) + 1)

    # Print the DataFrame
print("Print the DataFrame: ")
print(df)
print()

    #2.2
    # Save DataFrame to a .csv file with tabulation (\t) as separator
df.to_csv('output.csv', sep='\t', index=False) 

    #2.3
    # Load the DataFrame from the saved .csv file
df = pd.read_csv('output.csv', sep='\t')

    # Print the loaded DataFrame
print("Print the loaded DataFrame: ")
print(df)
print()


#Partie 3

    #3.1
    # Display the size of the corpus (number of documents)
corpus_size = df.shape[0]
print("Corpus size:", corpus_size)

    #3.2
    # Iterate over each document in the DataFrame
for index, row in df.iterrows():
    # Get the text of the document
    text = row['Text']
    
    # Check if the text is a string
    if isinstance(text, str):
        # Split the text into words and sentences
        words = text.split(' ')
        sentences = text.split('.')
        
        # Remove empty elements from the list of sentences
        sentences = list(filter(None, sentences))
        
        # Get the number of words and sentences
        num_words = len(words)
        num_sentences = len(sentences)
        
        # Print the results
        print("Document", index+1)
        print("Number of words:", num_words)
        print("Number of sentences:", num_sentences)
        print()

        #3.3
    # Filter documents with less than 20 characters
df = df[df['Text'].str.len() >= 20]

    # Print the updated corpus size
corpus_size = len(df)
print("Corpus size after removing short documents:", corpus_size)

        #3.4
    # Join all documents into a single string
corpus_string = ' '.join([text for text in df['Text']])

    # Print the corpus string
print("Corpus String:")
print(corpus_string)
