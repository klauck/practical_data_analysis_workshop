import sqlite3


drop_table_sql = "DROP TABLE IF EXISTS movie;"

create_table_sql =  """CREATE TABLE movie (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(250)
);"""

inserts_sql = [
    "INSERT INTO movie VALUES (1, 'Star Wars', 'sciFi');",
    "INSERT INTO movie VALUES (2, 'Star Trek', 'sciFi');",
    "INSERT INTO movie VALUES (3, 'Rocky', 'action');",
]


connection = sqlite3.connect("dbpra_example.db")

cursor = connection.cursor()
cursor.execute(drop_table_sql)
cursor.execute(create_table_sql)
for sql in inserts_sql:
    cursor.execute(sql)


cursor.execute("SELECT genre, count(*) FROM movie GROUP BY genre")
result = cursor.fetchall()

print(result)

import matplotlib.pyplot as plt

x = []
y = []

for genre, count in result:
    x.append(genre)
    y.append(count)

plt.yticks([0, 1, 2])
plt.bar(x, y)
plt.show()
