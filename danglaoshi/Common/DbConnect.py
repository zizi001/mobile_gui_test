# 数据库连接
import pymysql

db = None
cursor = None


# 连接数据库
def db_open():
    global db
    db = pymysql.connect(
        host='123.207.33.154',
        port=3306,
        user='root',
        passwd='dls@abc./*-',
        db='dlsj',
        charset='utf8'
    )
    global cursor
    cursor = db.cursor()


# 关闭数据库
def db_close():
    db.close()


# 插入、删除、更新(返回受影响行数)
def db_insert_delete_update(sql):
    i = None
    try:
        i = cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    return i


# 查询
def db_select(sql):
    results = None
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    return results
