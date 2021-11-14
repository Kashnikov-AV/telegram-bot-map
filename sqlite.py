import sqlite3
conn = sqlite3.connect('place.db')

cursor = conn.cursor()
cursor.execute("""CREATE TABLE place
                (pk integer not null primary key, user_id integer, name text, address text)
               """)
conn.commit()
conn.close()