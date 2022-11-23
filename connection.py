import pymysql

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdatabase",
        charset="utf8"
    )



def query_data(sql):
    conn= get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql):
    conn= get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()


# insert_or_update_data("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, PersonId int PRIMARY KEY AUTO_INCREMENT)")

insert_or_update_data("INSERT INTO Person(name,age,) VALUES ('Bari',32)")


