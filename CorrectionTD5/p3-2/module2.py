#3.2
        #Updating file Document.py , so we can include a type field and implement the getType() method in the child classes RedditDocument and ArxivDocument.  
from Document import RedditDocument, ArxivDocument
from Corpus import Corpus
from datetime import datetime

corpus = Corpus("My Corpus")

reddit_doc = RedditDocument("3PL", "Europe", "10 September 2022", "https://reddit.com", "Sth about douple brokerage", 10)
corpus.add_document(1, reddit_doc)

arxiv_doc = ArxivDocument("Logistics", ["USA", "Canada"], "15 October 2022", "https://arxiv.org", "Sth about usual lodistics")
corpus.add_document(2, arxiv_doc)

    # Print the documents in the corpus
for doc_id, doc in corpus.id2doc.items():
    print(f"Document ID: {doc_id}")
    print(f"Type: {doc.get_type()}")
    print(doc)
    print()

