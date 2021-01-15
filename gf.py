from django.db import connection
c=connection.cursor()
c.execute("select * from booking")
d=c.fetchall()
print(d)
