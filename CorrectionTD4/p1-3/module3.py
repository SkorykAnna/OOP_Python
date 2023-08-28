#1.3
    #Here's the modified code that allows to instantiate Document objects, import the module, and store the instances in a dictionary called id2doc:
#from datetime import datetime

#class Document:
#    def __init__(self, titre, auteur, date, url, texte):
#        self.titre = titre
#        self.auteur = auteur
#        self.date = datetime.strptime(date.strip(), "%d %B %Y").date()
#        self.url = url
#        self.texte = texte

#    def display_info(self):
#        print("Document Information:")
#        print(f"Title: {self.titre}")
#        print(f"Auteur: {self.auteur}")
#        print(f"Date: {self.date}")
#        print(f"URL: {self.url}")
#        print(f"Text: {self.texte}")

#    def __str__(self):
#        return f"Document: {self.titre}"


    # Create an instance of Document
#doc1 = Document("Logistics Coordination Based on Inventory Management and Transportation Planning by Third-Party Logistics (3PL)",
#                "Mariusz Kmiecik",
#                "4 July 2022",
#                "https://www.mdpi.com/2071-1050/14/13/8134",
#                "Currently, there is still a strong trend in research and in the market connected with the role of 3PL (third-party logistics) companies and the trend of developing and creating coordination in logistics networks.")

    # Create another instance of Document
#doc2 = Document("The role of an integrated logistics and procurement service offered by a 3PL firm in supply chain",
#                "Jingcheng Yang & Kai Yu",
#                "24 January 2019",
#                "https://www.tandfonline.com/doi/full/10.1080/23270012.2019.1568921",
#                "As an integrated part in supply chain, third-party logistics (3PL) has intrinsic connections with upstream manufacturer and downstream retailer.")

import praw
from datetime import datetime
from Document import Document

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

# Create a dictionary to store the Document instances
id2doc = {}

# Generate unique identifiers for the documents and store them in id2doc
for i, text in enumerate(texts, start=1):
    doc = Document(f"Reddit Document {i}", "Unknown", datetime.now().date(), "", text)
    id2doc[i] = doc

# Print the information of each document
for doc_id, doc in id2doc.items():
    print(f"Document ID: {doc_id}")
    doc.display_info()
    print()

# Print the size of the corpus
corpus_size = len(id2doc)
print(f"Corpus size: {corpus_size}")
