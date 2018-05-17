import psycopg2
# make connection with news database
db = psycopg2.connect("dbname = news")
# Allows Python code to execute PostgreSQL command in a database session
cur = db.cursor()

print "the most popular three articles of all time"
# this line to execute the database query
cur.execute("""select title,count(path) from log,articles where slug=SUBSTRING(path,10) group by(title) order by count(path) DESC limit 3 """)
rows = cur.fetchall()
# For loop to get all fetched data from the query
for row in rows:
    print row, "views" 

print "the most popular article authors of all time"
# this line to execute the database query
cur.execute(""" select name,count(name) from authors, log,articles  where slug=SUBSTRING(path,10) and authors.id = articles.author group by(name) order by count(name) DESC """)
rows2 = cur.fetchall()
# For loop to get all fetched data from the query
for row2 in rows2:
    print row2, "Views"

print "days did more than 1% of requests lead to errors"

# this line to execute the database query
cur.execute("""select * from error_rate order by date""")
rows3 = cur.fetchall()
# For loop to get all fetched data from the query
for row3 in rows3:
    print row3, "% errors"
    
