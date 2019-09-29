import os
import re

import sys
import pickle
import re
import  codecs
import string
import shutil
from win32com import client as wc
import docx
from docx import Document


def doSaveAas(name1,name2):

    doc = word.Documents.Open(name1)        # 目标路径下的文件
    doc.SaveAs('D:\\MyUniversityData\\GitHubRepository\\WordHandler\\newcet4\\'+name2+'.docx', 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()



def ReadFile2():
    root = 'D:\MyUniversityData\GitHubRepository\WordHandler\CET4'
    result=list()
    for parent, dirname, filenames in os.walk(root):

        for filename in filenames:
            if filename.endswith(".doc"):
                result.append(parent+'\\'+filename)
                doSaveAas(parent+'\\'+filename,filename[0:-4])

def ReadFile(name):
    root = 'D:\MyUniversityData\GitHubRepository\WordHandler\\'+name
    result=list()
    for parent, dirname, filenames in os.walk(root):

        for filename in filenames:
            if filename.endswith(".docx"):
                result.append(parent+'\\'+filename)

    #for item in result:
    #    print(item)

    print(result[0])
    for name in result:
        docx1=Document(name)
        f=open('AllZ4.txt','a',encoding='utf-8')
        for index,para in enumerate(docx1.paragraphs):
            f.write(para.text)
        f.close()











if __name__ == "__main__":
    '''
    word = wc.Dispatch('Word.Application')
    ReadFile()
    word.Quit()
    Transfer DOC to DOCX
    '''
    word = wc.Dispatch('Word.Application')
    ReadFile("newcet4")
    word.Quit()
    #ReadFile('newZ4')

