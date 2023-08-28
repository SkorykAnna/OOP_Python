        #3.1 
        # Using the Corpus class polmorism
from Document import ArxivDocument, RedditDocument
from Corpus import Corpus


# Create a Corpus object
corpus = Corpus("My Corpus")

# Create instances of ArxivDocument and RedditDocument:
arxiv_doc = ArxivDocument("Arxiv Title", ["Author 1", "Author 2"], "10 September 2022", "arxiv-url", "Arxiv Text")
reddit_doc = RedditDocument("Reddit Title", "Reddit Author", "15 October 2022", "reddit-url", "Reddit Text", 20)

# Add the documents to the corpus using the add_document method:
corpus.add_document(1, arxiv_doc)
corpus.add_document(2, reddit_doc)

    #Test the polymorphism by calling the methods specific to each document type:
# ArxivDocument-specific method
arxiv_auteurs = arxiv_doc.get_auteurs()
print(f"Arxiv Document Authors: {', '.join(arxiv_auteurs)}")

# RedditDocument-specific method
reddit_comments = reddit_doc.get_nb_comments()
print(f"Reddit Document Number of Comments: {reddit_comments}")

print(corpus)

