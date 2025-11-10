listaCarti = []

class Carte:
    def __init__(self, name, author, genre, launchYear, pages):
        self.name = name
        self.author = author
        self.genre = genre
        self.launchYear = launchYear
        self.pages = pages


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
        
class Library:

    def __add_carte__(self, name, author, genre, launchYear, pages):
        carte = Carte(name, author, genre, launchYear, pages)
        listaCarti.append(carte)

    def __filter_autor(author):
        # Filtered search dupa author, va afisa doar cartilor scrise de autorul respectiv
        return author


    def __filter_genre(genre):
        return genre # placeholder


# Concept menu screen

print("~-~-~-~-~-~-~-~-~-~-~-~")
print(" Bibliotheca Virtualis ")
print("~-~-~-~-~-~-~-~-~-~-~-~\n")

print("Cu ce te putem ajuta?\n")

# while (1):
