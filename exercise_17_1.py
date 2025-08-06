import sqlite3

# cnnect to the books database
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

# 1. display all authors (first, last) sorted by last then first
print("Authors (sorted by last, first):")
cursor.execute("SELECT first, last FROM authors ORDER BY last, first;")
for first, last in cursor.fetchall():
    print(f"{first} {last}")

# 2. display all book titles in ascending
print("\nBook titles (sorted):")
cursor.execute("SELECT title FROM titles ORDER BY title;")
for title, in cursor.fetchall():
    print(title)

# 3. display titles with copyright years, newest first
print("\nTitles with copyright (newest first):")
cursor.execute("SELECT title, copyright FROM titles ORDER BY copyright DESC;")
for title, copyright in cursor.fetchall():
    print(f"{title} ({copyright})")

# 4. display authors and books they written
print("\nAuthors and their books:")
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

# 5.display authors who have written more than one book
print("\nAuthors with more than one book:")
query = """
SELECT first || ' ' || last AS author, COUNT(*) as book_count
FROM authors
JOIN author_ISBN ON authors.id = author_ISBN.id
GROUP BY author
HAVING COUNT(*) > 1
ORDER BY book_count DESC;
"""
cursor.execute(query)
for author, count in cursor.fetchall():
    print(f"{author}: {count} books")

# close database connection
connection.close()
