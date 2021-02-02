import pymongo
from pymongo import MongoClient
from gridfs import *
import os

# myclientdata = pymongo.MongoClient("mongodb+srv://peter:0987602620@cluster0.0qqo9.mongodb.net/ceb101?retryWrites=true&w=majority")
# mydbdata = myclientdata['test']
# mycoldata = mydbdata['trash']
# print(mydbdata)

# results = mydbdata.find({})
# for result in results:
#     print(result)




# datatmp = open('./img/8.jpg', 'rb')
# #建立寫入流
# imgput = GridFS(mydbdata)
# #將資料寫入，檔案型別和名稱通過前面的分割得到
# insertimg=imgput.put(datatmp,filename='2')
#
# print("js")

#從MONGO抓照片
import pymongo
from pymongo import MongoClient
from gridfs import *

myclientdata = pymongo.MongoClient("mongodb+srv://peter:0987602620@cluster0.0qqo9.mongodb.net/ceb101?retryWrites=true&w=majority")
mydbdata = myclientdata['test']
mycoldata = mydbdata['trash']

#給予girdfs模組來寫出，其中collection為上一步生成的，我不知道怎麼該名稱。實際上是由fs.flies和fs.chunks組成
gridFS = GridFS(mydbdata, collection="fs")
count=0
for grid_out in gridFS.find():
    count+=1
    print(count)
    data = grid_out.read() # 獲取圖片資料
    outf = open('%s.jpg' %(count),'wb')#建立檔案
    outf.write(data)  # 儲存圖片
    outf.close()