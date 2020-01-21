import psycopg2

conn = psycopg2.connect("host=127.0.0.1 dbname=udacity user=student password=student")
cur = conn.cursor()
conn.set_session(autocommit=True)
cur.execute("CREATE TABLE test123 (col1 int, col2 int, col3 int);")
cur.execute("select * from test123")
cur.execute("select count(*) from test123")
print(cur.fetchall())
cur.execute("drop table test123")

