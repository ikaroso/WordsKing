'''
输入是一个单词list

推荐的算法：
1.通过一个个的单词，先选出这个单词在coca里的词频，然后根据其在所属类别的词频推荐
2.通过一串单词，找出对应coca词频，根据某种算法算出在对应类别里的词频，然后推荐

考虑：
如果仅仅分别考虑，可能无法准确体现出难度，因为单词之间也许存在着某种联系，某个词频高，某个词频低
全部考虑的话，怎么找这个算法

目前：
先实现每一个都通过第一种方法推荐，实现一个小demo
'''
import pymysql


def recommend1(wordlist:'list'):
    print(str(len(wordlist))+' words input in total')

    sql1 = "select * from cet4"
    conn = pymysql.connect(host="localhost", user="root",password="123",database="WordsKing",charset="utf8")
    cursor=conn.cursor()

    for word in wordlist:
        print('recommending by using '+word)
        cursor.execute(sql1)
        result=cursor.fetchall()
        print(len(result))
        for item in result:
            print(item)




    conn.commit()
    cursor.close()
    conn.close()

'''
先找到它在coca里的总词频
根据他所属的类别（user正在使用的单词表）找到对应数据库
推荐词频相近单词【难点出现了，应该如何推荐】
'''



if __name__ == "__main__":
    x=list()

    recommend1(x)
