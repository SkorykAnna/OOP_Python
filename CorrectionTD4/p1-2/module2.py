#1.2
    #was updated Document.py file with such code:
#class Document:
#    def __init__(self, titre, auteur, date, url, texte):
#        self.titre = titre
#        self.auteur = auteur
#        self.date = date
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
from Document import Document

doc = Document("Logistics Coordination Based on Inventory Management and Transportation Planning by Third-Party Logistics (3PL)",
               "Mariusz Kmiecik",
               "4 July 2022",
               "https://www.mdpi.com/2071-1050/14/13/8134",
               "Currently, there is still a strong trend in research and in the market connected with the role of 3PL (third-party logistics) companies and the trend of developing and creating coordination in logistics networks.")

    # Call display_info() method
doc.display_info()

    # Call __str__() method implicitly when using print()
print(doc)
