what are we reporting?
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 


Requirements:
python2 or 3
postgresql
psycopg2


The created views

//this is a view from real data that calculate the number of requests that can't access the site in specific date

cur.execute("""create view errors  AS SELECT date(time), COUNT(*) AS not_found FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time) 
ORDER BY date(time)""")

//this is a view from real data that calculate all the number of requests that  access the site in specific date

cur.execute("""create view all_view as select date(time) , count(*)as views  from log group by date(time) order by date(time)""")

//this is a view from real data that calculate a percentage of requests that can't  access the site in specific date

cur.execute("""create view error_rate as select all_view.date,(errors.not_found*100/all_view.views) as date_error  
from errors,all_view 
where errors.date=all_view.date and (errors.not_found*100/all_view.views)>1""")
