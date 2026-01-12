from carte import Carte

listaCarti = [
    Carte("Poor Folk", "Fyodor Dostoyevsky", "Fiction", 1846, 271,
          "https://covers.openlibrary.org/b/title/Poor%20Folk-L.jpg"),

    Carte("White Nights", "Fyodor Dostoyevsky", "Fiction", 1848, 120,
          "https://covers.openlibrary.org/b/title/White%20Nights-L.jpg"),

    Carte("Crime and Punishment", "Fyodor Dostoyevsky", "Fiction", 1866, 671,
          "https://covers.openlibrary.org/b/title/Crime%20and%20Punishment-L.jpg"),

    Carte("The Gambler", "Fyodor Dostoyevsky", "Fiction", 1867, 210,
          "https://covers.openlibrary.org/b/title/The%20Gambler-L.jpg"),

    Carte("The Idiot", "Fyodor Dostoyevsky", "Fiction", 1869, 656,
          "https://covers.openlibrary.org/b/title/The%20Idiot-L.jpg"),

    Carte("Demons", "Fyodor Dostoyevsky", "Political Fiction", 1872, 768,
          "https://covers.openlibrary.org/b/title/Demons-L.jpg"),

    Carte("The Brothers Karamazov", "Fyodor Dostoyevsky", "Philosophical Fiction", 1880, 824,
          "https://covers.openlibrary.org/b/title/The%20Brothers%20Karamazov-L.jpg"),

    Carte("War and Peace", "Leo Tolstoy", "Historical Fiction", 1869, 1225,
          "https://covers.openlibrary.org/b/title/War%20and%20Peace-L.jpg"),

    Carte("Anna Karenina", "Leo Tolstoy", "Fiction", 1877, 864,
          "https://covers.openlibrary.org/b/title/Anna%20Karenina-L.jpg"),

    Carte("The Death of Ivan Ilyich", "Leo Tolstoy", "Fiction", 1886, 86,
          "https://covers.openlibrary.org/b/title/The%20Death%20of%20Ivan%20Ilyich-L.jpg"),

    Carte("The Master and Margarita", "Mikhail Bulgakov", "Fantasy", 1967, 480,
          "https://covers.openlibrary.org/b/title/The%20Master%20and%20Margarita-L.jpg"),

    Carte("Dead Souls", "Nikolai Gogol", "Satire", 1842, 432,
          "https://covers.openlibrary.org/b/title/Dead%20Souls-L.jpg"),

    Carte("Fathers and Sons", "Ivan Turgenev", "Fiction", 1862, 244,
          "https://covers.openlibrary.org/b/title/Fathers%20and%20Sons-L.jpg"),

    Carte("1984", "George Orwell", "Dystopian", 1949, 328,
          "https://covers.openlibrary.org/b/title/1984-L.jpg"),

    Carte("Animal Farm", "George Orwell", "Political Satire", 1945, 112,
          "https://covers.openlibrary.org/b/title/Animal%20Farm-L.jpg"),

    Carte("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 281,
          "https://covers.openlibrary.org/b/title/To%20Kill%20a%20Mockingbird-L.jpg"),

    Carte("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 180,
          "https://covers.openlibrary.org/b/title/The%20Great%20Gatsby-L.jpg"),

    Carte("Lord of the Flies", "William Golding", "Allegorical Fiction", 1954, 224,
          "https://covers.openlibrary.org/b/title/Lord%20of%20the%20Flies-L.jpg"),

    Carte("Brave New World", "Aldous Huxley", "Dystopian", 1932, 268,
          "https://covers.openlibrary.org/b/title/Brave%20New%20World-L.jpg"),

    Carte("Dune", "Frank Herbert", "Science Fiction", 1965, 412,
          "https://covers.openlibrary.org/b/title/Dune-L.jpg"),

    Carte("Foundation", "Isaac Asimov", "Science Fiction", 1951, 255,
          "https://covers.openlibrary.org/b/title/Foundation-L.jpg"),

    Carte("Neuromancer", "William Gibson", "Cyberpunk", 1984, 271,
          "https://covers.openlibrary.org/b/title/Neuromancer-L.jpg"),

    Carte("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction", 1979, 224,
          "https://covers.openlibrary.org/b/title/The%20Hitchhiker%27s%20Guide%20to%20the%20Galaxy-L.jpg"),

    Carte("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 310,
          "https://covers.openlibrary.org/b/title/The%20Hobbit-L.jpg"),

    Carte("The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy", 1954, 423,
          "https://covers.openlibrary.org/b/title/The%20Fellowship%20of%20the%20Ring-L.jpg"),

    Carte("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 332,
          "https://covers.openlibrary.org/b/title/Harry%20Potter%20and%20the%20Philosopher%27s%20Stone-L.jpg"),

    Carte("Dracula", "Bram Stoker", "Horror", 1897, 418,
          "https://covers.openlibrary.org/b/title/Dracula-L.jpg"),

    Carte("Frankenstein", "Mary Shelley", "Gothic Fiction", 1818, 280,
          "https://covers.openlibrary.org/b/title/Frankenstein-L.jpg"),

    Carte("The Shining", "Stephen King", "Horror", 1977, 447,
          "https://covers.openlibrary.org/b/title/The%20Shining-L.jpg"),

    Carte("Meditations", "Marcus Aurelius", "Philosophy", 180, 256,
          "https://covers.openlibrary.org/b/title/Meditations-L.jpg"),

    Carte("Beyond Good and Evil", "Friedrich Nietzsche", "Philosophy", 1886, 240,
          "https://covers.openlibrary.org/b/title/Beyond%20Good%20and%20Evil-L.jpg"),

    Carte("The Republic", "Plato", "Philosophy", -380, 416,
          "https://covers.openlibrary.org/b/title/The%20Republic-L.jpg"),

    Carte("Sapiens", "Yuval Noah Harari", "History", 2011, 443,
          "https://covers.openlibrary.org/b/title/Sapiens-L.jpg"),

    Carte("Man's Search for Meaning", "Viktor Frankl", "Psychology", 1946, 200,
          "https://covers.openlibrary.org/b/title/Man%27s%20Search%20for%20Meaning-L.jpg"),

    Carte("The Art of War", "Sun Tzu", "Strategy", -500, 112,
          "https://covers.openlibrary.org/b/title/The%20Art%20of%20War-L.jpg"),

    Carte("The Road", "Cormac McCarthy", "Post-Apocalyptic", 2006, 287,
          "https://covers.openlibrary.org/b/title/The%20Road-L.jpg"),

    Carte("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 277,
          "https://covers.openlibrary.org/b/title/The%20Catcher%20in%20the%20Rye-L.jpg")
]