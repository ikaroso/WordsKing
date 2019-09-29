#D:\MyUniversityData\GitHubRepository\WordHandler\all
import string
import  re
import pymysql
'''

还要解决不同词形的问题
'''


def DBquery():
    total=list()

    print("hello")
    conn = pymysql.connect(host="localhost", user="root",password="123",database="WordsKing",charset="utf8")
    cursor=conn.cursor()

    sql1 = "select * from cet4"
    cursor.execute(sql1)
    result=cursor.fetchall()
    print(len(result))
    for item in result:
        total.append(item)

    sql1 = "select * from cet6"
    cursor.execute(sql1)
    result=cursor.fetchall()
    print(len(result))

    for item in result:
        total.append(item)
    sql1 = "select * from z4"
    cursor.execute(sql1)
    result=cursor.fetchall()
    print(len(result))
    for item in result:
        total.append(item)

    sql1 = "select * from z8"
    cursor.execute(sql1)
    result=cursor.fetchall()
    print(len(result))
    for item in result:
        total.append(item)


    print(total[0])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":

    #DBquery()
    #这个函数目前并没有写好
    print('Not ok yet')
