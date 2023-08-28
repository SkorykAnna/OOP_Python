import pandas as pd
from datetime import datetime
from Author import Author
from Document import Document

class Corpus:
    def __init__(self, name):
        self.nom = name
        self.authors = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

    def add_document(self, doc_id, doc):
        # Check if the author is known
        if doc.auteur not in self.authors:
            # Create a new Author instance
            author = Author(doc.auteur)
            # Add the Author instance to the authors dictionary
            self.authors[doc.auteur] = author
            self.naut += 1
        else:
            author = self.authors[doc.auteur]
        # Add the Document instance to the id2doc dictionary
        self.id2doc[doc_id] = doc
        self.ndoc += 1
        # Add the document to the author's production
        author.add_document(doc_id, doc)
    
    def display_documents_with_source(self):
        for doc_id, doc in self.id2doc.items():
            doc_type = doc.get_type()
            print(f"Document ID: {doc_id}, Source: {doc_type}, {doc.titre}")


    def __str__(self):
        return f"Corpus: {self.nom}\nNumber of Documents: {self.ndoc}\nNumber of Authors: {self.naut}"

    def sort_documents_by_date(self, limit=None):
        sorted_docs = sorted(self.id2doc.values(), key=lambda x: x.date)
        if limit:
            sorted_docs = sorted_docs[:limit]
        for doc in sorted_docs:
            doc.display_info()
            print()

    def sort_documents_by_title(self, limit=None):
        sorted_docs = sorted(self.id2doc.values(), key=lambda x: x.titre)
        if limit:
            sorted_docs = sorted_docs[:limit]
        for doc in sorted_docs:
            doc.display_info()
            print()

    def __repr__(self):
        return f"Corpus: {self.nom}, Documents: {self.ndoc}, Authors: {self.naut}"

    def save(self, filename):
        # Create a DataFrame to store the corpus data
        data = {
            "doc_id": [],
            "titre": [],
            "auteur": [],
            "date": [],
            "url": [],
            "texte": []
        }
        for doc_id, doc in self.id2doc.items():
            data["doc_id"].append(doc_id)
            data["titre"].append(doc.titre)
            data["auteur"].append(doc.auteur)
            data["date"].append(doc.date)
            data["url"].append(doc.url)
            data["texte"].append(doc.texte)
        df = pd.DataFrame(data)
        # Save the DataFrame to a file
        df.to_csv(filename, index=False)

    @staticmethod
    def load(filename):
        # Load the DataFrame from the file
        df = pd.read_csv(filename)
        corpus = Corpus("Loaded Corpus")
        for i, row in df.iterrows():
            doc_id = row["doc_id"]
            titre = row["titre"]
            auteur = row["auteur"]
            date_str = row["date"]
            date = datetime.strptime(date_str, "%d %B %Y").date()
            url = row["url"]
            texte = row["texte"]
            doc = Document(titre, auteur, date, url, texte)
            corpus.add_document(doc_id, doc)
        return corpus

