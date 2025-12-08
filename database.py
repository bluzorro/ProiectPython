import hashlib
import os
import sqlite3
from datetime import datetime


def initDB():
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print("Initializing Database")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            coverPath TEXT,
            available INTEGER NOT NULL DEFAULT 1
        )
    """)

    # Carti imprumutate

    cur.execute("""
        CREATE TABLE IF NOT EXISTS borrowedBooks
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            book TEXT NOT NULL,
            user TEXT NOT NULL
        )
    """)

    # Users

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)

    # print("DB initialised")

    conn.commit()
    conn.close()


initDB()


def insertInitialBooks(book_list):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    for b in book_list:
        cur.execute("""
            INSERT INTO books (name, author, genre, coverPath, available)
            VALUES (?, ?, ?, ?, ?)
        """, (b.name, b.author, b.genre, b.coverPath, 1))

    conn.commit()
    conn.close()




def loadAvailableBooks():
    # print("Loading available books...")
    from classes import (Carte)
    # print("Imported Carte")
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    cur.execute("SELECT name, author, genre, launchYear, pages, coverPath FROM books WHERE available = 1")
    rows = cur.fetchall()

    conn.close()

    # print("Am fetchuit toate cartile!")
    # print(rows)

    availableBooks = []
    for (name, author, genre, launchYear, pages, coverPath) in rows:
        # print(name, author, genre)
        availableBooks.append(Carte(name, author, genre, launchYear, pages, coverPath))

    # print("Am convertit intr-o lista tot")


    return availableBooks


def isBookAvailable(bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # vedem dacă exista in borrowedBooks
    cur.execute("SELECT 1 FROM borrowedBooks WHERE book = ?", (bookName,))
    row = cur.fetchone()

    conn.close()

    return row is None   # daca nu exista, cartea e disponibila




def borrowBook(username, bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # verificam dacă e deja imprumutata
    cur.execute("SELECT 1 FROM borrowedBooks WHERE book = ?", (bookName,))
    row = cur.fetchone()

    if row is not None:
        conn.close()
        return False  # carte indisponibila

    # altfel o imprumutam
    now = datetime.now()
    formattedNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(formattedNow)  # ex: "2025-02-14 23:59:01"
    cur.execute(
        "INSERT INTO borrowedBooks (book, user, borrowDate) VALUES (?, ?, ?)",
        (bookName, username, formattedNow)
    )

    cur.execute("UPDATE books SET available = 0 WHERE name = ?", (bookName,))

    conn.commit()
    conn.close()
    return True




def returnBook(username, bookName):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # ștergem doar daca user-ul a imprumutat-o
    print("Sterge? " + username + bookName)
    cur.execute(
        "DELETE FROM borrowedBooks WHERE book = ? AND user = ?",
        (bookName, username)
    )

    print("Sters!")

    cur.execute("UPDATE books SET available = 1 WHERE name = ?", (bookName,))

    print("updated!")

    changes = conn.total_changes
    conn.commit()
    conn.close()

    return changes > 0   # True daca s-a returnat, False daca nu era imprumutata



def getBorrowedBooks(username):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()


    cur.execute("SELECT book FROM borrowedBooks WHERE user = ?", (username,))
    rows = cur.fetchall()

    conn.close()

    return [row[0] for row in rows]

def hashPassword(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()

    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed, salt


def authenticateUser(username, password):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print(username, password)
    cur.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    row = cur.fetchone()

    # print(row)



    if row is None:
        # user nu exista, creeam noi
        # print("Creeam user!")
        input_hash, salt = hashPassword(password)
        # print("Adaugam user in tabel")
        cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, input_hash, salt,))
        conn.commit()

    cur.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    # print(row)
    stored_hash, salt = row
    input_hash, _ = hashPassword(password, salt)


    return input_hash == stored_hash


def isAdmin(username):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()
    cur.execute("SELECT username FROM admins WHERE username = ?", (username,))
    row = cur.fetchone()
    # print(row)

    return row is not None


def insert_book(book):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # evitam cartile duplicate
    cur.execute("SELECT id FROM books WHERE name = ? AND author = ?",
                (book.name, book.author))

    if cur.fetchone() is not None:
        conn.close()
        return False  # deja exista

    cur.execute("""
        INSERT INTO books(name, author, genre, launchYear, pages, coverPath)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        book.name,
        book.author,
        book.genre,
        book.launchYear,
        book.pages,
        book.coverPath,
    ))

    conn.commit()
    conn.close()
    return True


def getElapsedTime(book):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print("Cautam borrowDate in db pt " + book.name)

    cur.execute("SELECT borrowDate FROM borrowedBooks WHERE book = ?", (book.name,))
    row = cur.fetchone()

    print(row)
    if row is None:
        conn.close()
        # Cartea nu e imprumutata
        return 0

    now = datetime.now()
    then = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
    delta = now - then

    # print("Delta: " + str(delta))

    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if days > 0:
        return f"acum {days} zile"
    elif hours > 0:
        return f"acum {hours} ore"
    elif minutes > 0:
        return f"acum {minutes} minute"
    else:
        return "chiar acum"



def hashPassword(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()

    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed, salt


def authenticateUser(username, password):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print(username, password)
    cur.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    row = cur.fetchone()

    # print(row)



    if row is None:
        # user nu exista, creeam noi
        # print("Creeam user!")
        input_hash, salt = hashPassword(password)
        # print("Adaugam user in tabel")
        cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, input_hash, salt,))
        conn.commit()

    cur.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    # print(row)
    stored_hash, salt = row
    input_hash, _ = hashPassword(password, salt)


    return input_hash == stored_hash


def isAdmin(username):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()
    cur.execute("SELECT username FROM admins WHERE username = ?", (username,))
    row = cur.fetchone()
    # print(row)

    return row is not None


def insertBook(book):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # evitam cartile duplicate
    cur.execute("SELECT id FROM books WHERE name = ? AND author = ?",
                (book.name, book.author))

    if cur.fetchone() is not None:
        conn.close()
        return False  # deja exista

    cur.execute("""
        INSERT INTO books(name, author, genre, launchYear, pages, coverPath)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        book.name,
        book.author,
        book.genre,
        book.launchYear,
        book.pages,
        book.coverPath,
    ))

    conn.commit()
    conn.close()
    return True


def getElapsedTime(book):
    conn = sqlite3.connect("libraryDB")
    cur = conn.cursor()

    # print("Cautam borrowDate in db pt " + book.name)

    cur.execute("SELECT borrowDate FROM borrowedBooks WHERE book = ?", (book.name,))
    row = cur.fetchone()

    # print(row)
    if row is None:
        conn.close()
        # Cartea nu e imprumutata
        return 0

    now = datetime.now()
    then = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
    delta = now - then

    # print("Delta: " + str(delta))

    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if days > 0:
        return f"acum {days} zile"
    elif hours > 0:
        return f"acum {hours} ore"
    elif minutes > 0:
        return f"acum {minutes} minute"
    else:
        return "chiar acum"

