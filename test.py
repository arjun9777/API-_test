import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table ="CREATE TABLE users (id int, username text, password text)" #This defines what we call it as schema that tells how our data is going to look"
cursor.execute(create_table)


user = (1, 'arjun', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()


