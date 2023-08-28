    #2.1 
    # Adding to Document.py class ArxivDocument
from datetime import datetime

class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = datetime.strptime(date, "%d %B %Y").date()
        self.url = url
        self.texte = texte
        self.type = "Document"  # Added firal "type" with input "Document"

    def get_type(self):
        return self.type

    def __str__(self):
        return f"Title: {self.titre}\nAuthor: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}"

class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, nb_comments):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_comments = nb_comments
        self.type = "Reddit" 

    def get_nb_comments(self):
        return self.nb_comments

    def set_nb_comments(self, nb_comments):
        self.nb_comments = nb_comments

    def __str__(self):
        # Call the __str__ method of the parent class (Document)
        return super().__str__() + f"\nNumber of Comments: {self.nb_comments}"

class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, None, date, url, texte)
        self.auteurs = auteurs
        self.type = "Arxiv" 

    def get_auteurs(self):
        return self.auteurs

    def set_auteurs(self, auteurs):
        self.auteurs = auteurs

    def __str__(self):
        # Call the __str__ method of the parent class (Document)
        return super().__str__() + f"\nAuthors: {', '.join(self.auteurs)}"