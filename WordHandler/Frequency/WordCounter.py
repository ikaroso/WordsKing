#D:\MyUniversityData\GitHubRepository\WordHandler\all
import string
import  re
import pymysql
'''
最好是分类保存成三个json文件
还要解决不同词形的问题
'''
def FindEngWord(name):
    result={}

    f=open(name,'r',encoding='utf-8')
    st=f.read()
    s=re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",st)
    s=s.lower()
    r=s.split()
    for item in r:
        result[item]=result.get(item,0)+1

    f.close()
    items=list(result.items())
    items.sort(key=lambda x:x[1], reverse=True)

    return items

def getjson(namex):
    name={}

def DBwrite(cet4,cet6,z4,z8):
    print("hello")
    conn = pymysql.connect(host="localhost", user="root",password="123",database="WordsKing",charset="utf8")
    cursor=conn.cursor()
    sql1 = "insert into cet4(word,frequency) values(%s, %s)"
    sql2 = "insert into cet6(word,frequency) values(%s, %s)"
    sql3 = "insert into z4(word,frequency) values(%s, %s)"
    sql4 = "insert into z8(word,frequency) values(%s, %s)"


    for item in cet4:
        cursor.execute(sql1, (item[0],item[1]))

    for item in cet6:
        cursor.execute(sql2, (item[0],item[1]))

    for item in z4:
        cursor.execute(sql3, (item[0],item[1]))

    for item in z8:
        cursor.execute(sql4, (item[0],item[1]))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    cet4x=FindEngWord('D:\\MyUniversityData\\GitHubRepository\WordHandler\\all\\Allcet4.txt')
    cet6x=FindEngWord('D:\\MyUniversityData\\GitHubRepository\WordHandler\\all\\Allcet6.txt')
    Z8x=FindEngWord('D:\\MyUniversityData\\GitHubRepository\WordHandler\\all\\AllZ8.txt')
    Z4x=FindEngWord('D:\\MyUniversityData\\GitHubRepository\WordHandler\\all\\AllZ4.txt')

    cet4={}
    cet6={}
    Z4={}
    Z8={}
    print(Z4x[152])
    DBwrite(cet4x,cet6x,Z4x,Z8x)


