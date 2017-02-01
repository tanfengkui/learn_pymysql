import pymysql

conn = pymysql.connect(host='localhost', user='root',password="",database="test")
# conn.query('create database test')

cursor = conn.cursor()
cursor.execute('select * from test')

row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

cursor.execute('select * from test')

for row in cursor:
    print('row = %r' % (row,))


conn.commit()

conn.close()
