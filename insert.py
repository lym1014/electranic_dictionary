import pymysql
a = open('./dict.txt','rt')
l = []
sql1 = pymysql.connect(host='localhost',user = 'root',password = 'lym653512',database = 'electranic_dictionary')
sql2 = sql1.cursor()
while True:
    b = a.readline()
    if not b:
        break
    x = b.split(' ',1)
    x[1] = x[1].strip()
    sql2.execute('insert into dictionary5 values(%s,%s)',[x[0],x[1]])
    sql1.commit()

sql2.close()
sql1.close()
a.close()








