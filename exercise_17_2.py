import sqlite3

# connect to the books database
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

# 1. list tables in database
print("All tables in books.db:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for table in cursor.fetchall():
    print(table[0])

# 2. list all authors (sorted by last then first)
print("\nAuthors (sorted):")
cursor.execute("SELECT first, last FROM authors ORDER BY last, first;")
for first, last in cursor.fetchall():
    print(f"{first} {last}")

# 3. list all bookstitles (sorted alphabet)
print("\nBook titles (sorted):")
cursor.execute("SELECT title FROM titles ORDER BY title;")
for title, in cursor.fetchall():
    print(title)

# 4. list all books w/ authors
print("\nBooks with authors:")
query = """
SELECT first || ' ' || last AS author, title
FROM authors
JOIN author_ISBN ON authors.id = author_ISBN.id
JOIN titles ON titles.isbn = author_ISBN.isbn
ORDER BY author, title;
"""
cursor.execute(query)
for author, title in cursor.fetchall():
    print(f"{author} – {title}")

# close database connect.
connection.close()
