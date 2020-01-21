import psycopg2

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)

conn.set_session(autocommit=True)

try:
    cur.execute("select * from udacity.music_library")
except psycopg2.Error as e:
    print(e)

try:
    cur.execute("create database udacity")
except psycopg2.Error as e:
    print(e)

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=udacity user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to Postgres database")
    print(e)


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the database")
    print(e)

conn.set_session(autocommit=True)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_library (album_name varchar, artist_name varchar, year int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("select count(*) from music_library")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)
print(cur.fetchall())


try:
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                VALUES (%s, %s, %s)", \
                ("Let It Be", "The Beatles", 1970))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                VALUES (%s, %s, %s)", \
                ("Rubber Soul", "The Beatles", 1965))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


try:
    cur.execute("SELECT * FROM music_library;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("DROP table music_library")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

cur.close()
conn.close()



