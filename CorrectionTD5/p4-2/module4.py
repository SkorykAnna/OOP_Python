        #4.2
        #In this implementation, we have an abstract base class Document that defines the common interface for all document types. 
        #The RedditDocument and ArxivDocument classes are concrete implementations of the Document class.
        #The DocumentFactory class acts as the factory that creates instances of the desired document type based on the given parameters. 
        #It has a static method create_document that takes in the document type, along with other necessary parameters, and returns 
        #an instance of the corresponding document class.
from Document import DocumentFactory

reddit_doc = DocumentFactory.create_document("reddit", "3PL", "Europe", "2022-06-01", "https://reddit.com", "Sth about double brokerage", comment_count=10)
arxiv_doc = DocumentFactory.create_document("arxiv", "Logistics", ["John", "Russ"], "2022-06-02", "https://arxiv.org", "Sth about usual logistics")



reddit_doc.display_info()
print()
arxiv_doc.display_info()