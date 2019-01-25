# -* encoding:utf-8 *-
import traceback
import pymysql
import time

def myexcept(len):
    if len < 1:
        raise Exception("IDNullError",len)

def connDB():
    print ("正在连接服务器....")
    conn = pymysql1.connect(
        host="34.235.86.20",
        user="sokamgrdev",
        password="sokamgr@Pwd",
        port=3306,
        charset="utf8mb4",
        db="sokadb"
    )
    print ("连接服务器成功")
    cur = conn.cursor()
    return (conn, cur)


def selectDB(cur, id):
    sql = "select * from article WHERE id = '%d'" % (id)
    joke = cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        print ("查询结束，数据库无数据，请重新输入id")
    else:
        for row in result:
            id = row[0]
            title = row[1]
            content = row[2]
            small_cover = row[3]
            create_time = row[9]
            print ("id:%d,title:%s,content:%s,small_cover:%s,create_time:%s") \
                  % (id, title, content, small_cover, create_time)
            return (joke)

def selectDBAuto(cur):
    sql = "select identity from identity"
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        print ("查询结束，数据库无数据，请重新输入id")
    else:
        return result

def deleteDB(conn, cur, id):
    sql = "delete * from article WHERE id = '%d'" % (id)
    joke = cur.execute(sql)
    conn.commit()
    return (joke)


def updateDB(conn, cur, name, id):
    sql1 = "select * from tag WHERE id = '%d'" % (id)
    cur.execute(sql1)
    result1 = cur.fetchall()
    try:
        myexcept(len(result1))
    except "IDNullError":
        print ("更新数据ID有误，请重新输入")
    else:
        sql2 = "update tag set name = '%s' WHERE id = '%d'" % (name, id)
        joke = cur.execute(sql2)
        conn.commit()
        return (joke)


def insertDB(conn, cur, sql):
    joke = cur.execute(sql)
    conn.commit()
    return (joke)


def closeDB(conn, cur):
    conn.close()
    cur.close()


def main_1():
    result = True
    conn, cur = connDB()
    print ("请选择以上四个操作：1、查询记录 2、删除记录 3、更新记录 4、增加记录.(按Q退出程序)")
    number = raw_input()
    while (result):
        if (number == 'q' or number == 'Q'):
            print("退出程序中...")
            time.sleep(3)
            break

        elif (int(number) == 1):
            id = input("请输入查询的文章ID：")
            try:
                selectDB(cur, id)
                print ("查询成功")
            except Exception, e:
                traceback.print_exc()
            finally:
                closeDB(conn,cur)

        elif (int(number) == 2):
            id = input("请输入删除的文章ID：")
            try:
                deleteDB(conn, cur, id)
                print("删除成功")
            except pymysql1.err.ProgrammingError as e:
                print ("删除的记录id在数据库中不存在")
            finally:
                closeDB(conn,cur)

        elif (int(number) == 3):
            name = raw_input("请输入更新的tag表名字：")
            id = input("请输入更新的tag表ID:")
            try:
                updateDB(conn, cur, name, id)
                print ("更新成功")
            except Exception as e:
                traceback.print_exc()
            closeDB(conn,cur)

        elif (int(number) == 4):
            sql = raw_input("请输入插入数据的sql语句:")
            try:
                insertDB(conn, cur, sql)
                print ("插入数据成功")
            except Exception as e:
                raise
            finally:
                closeDB(conn,cur)

        else:
            print ("非法输入，将结束进程")
            closeDB(conn, cur)
            print conn.open    #判断数据库连接状态
            break
        print ("请选择以上四个操作：1、查询记录 2、删除记录 3、更新记录 4、增加记录.(按Q退出程序)")
        number = raw_input("请选择操作")


if __name__ == "__main__":
    main_1()
