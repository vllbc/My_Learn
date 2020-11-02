import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='xwh5201314',db='mydb',port=3306,charset='utf8')
cursor = conn.cursor()
cursor.execute("insert into students (name,sex,grade) values('张三','女',83);")
conn.commit()
