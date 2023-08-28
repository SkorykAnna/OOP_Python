from abc import ABC, abstractmethod
from datetime import datetime

class Document(ABC):
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    @abstractmethod
    def display_info(self):
        pass

class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, comment_count):
        super().__init__(titre, auteur, date, url, texte)
        self.comment_count = comment_count

    def display_info(self):
        print(f"Reddit Document\nTitle: {self.titre}\nAuthor: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}\nComment Count: {self.comment_count}")

class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, auteurs, date, url, texte)
        self.auteurs = auteurs

    def display_info(self):
        authors_str = ', '.join(self.auteurs) if self.auteurs else "No author"
        print(f"Arxiv Document\nTitle: {self.titre}\nAuthors: {authors_str}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}")


class DocumentFactory:
    @staticmethod
    def create_document(doc_type, titre, auteurs, date, url, texte, comment_count=None):
        if doc_type == "reddit":
            return RedditDocument(titre, auteurs, date, url, texte, comment_count)
        elif doc_type == "arxiv":
            return ArxivDocument(titre, auteurs, date, url, texte)
        else:
            raise ValueError("Invalid document type.")