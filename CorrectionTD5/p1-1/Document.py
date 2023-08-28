    #1.1 RedditDocument
    # Was created file Document.py, there implemented class RedditDocument
from datetime import datetime

class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = datetime.strptime(date, "%d %B %Y").date()
        self.url = url
        self.texte = texte

    def __str__(self):
        return f"Title: {self.titre}\nAuthor: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nText: {self.texte}"

class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, nb_comments):
        # Call the constructor of the parent class (Document)
        super().__init__(titre, auteur, date, url, texte)
        # Add the specific attribute for RedditDocument
        self.nb_comments = nb_comments

    def get_nb_comments(self):
        return self.nb_comments

    def set_nb_comments(self, nb_comments):
        self.nb_comments = nb_comments

    def __str__(self):
        # Call the __str__ method of the parent class (Document)
        return super().__str__() + f"\nNumber of Comments: {self.nb_comments}"