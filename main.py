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
        listaCurenta.clear()
        for carte in listaCarti:
            if (author == carte.author):
                listaCurenta.append(carte)

        # Functie display/update display si afiseaza cartile care corespund filtrarii


    def __filter_genre(genre):
        listaCurenta.clear()
        for carte in listaCarti:
            if (genre == carte.genre):
                listaCurenta.append(carte)

        # Update display


listaCarti = [
    Carte("Poor Folk", "Fyodor Dostoyevsky", "Fiction", 1846, 271),
    Carte("White Nights", "Fyodor Dostoyevsky", "Fiction", 1848, 120),
    Carte("Crime and Punishment", "Fyodor Dostoyevsky", "Fiction", 1866, 671),
    Carte("The Gambler", "Fyodor Dostoyevsky", "Fiction", 1867, 210),
    Carte("The Idiot", "Fyodor Dostoyevsky", "Fiction", 1869, 656),

]  # de introdus sau fetch-ed

listaCurenta = [] # cartile ce vor fi afisate dupa search / filter

# Concept menu screen

print("~-~-~-~-~-~-~-~-~-~-~-~")
print(" Bibliotheca Virtualis ")
print("~-~-~-~-~-~-~-~-~-~-~-~\n")

print("Cu ce te putem ajuta?\n")

# while (1):
