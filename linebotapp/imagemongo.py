#照片放到MONGO

# myclient = pymongo.MongoClient(
#         "mongodb+srv://")
# mydb = myclient["mydatabase"]
# # mycol.insert_many([member])
# #本地硬碟上的圖片目錄
# dirs = './images3'
# #列出目錄下的所有圖片
# files = os.listdir(dirs)
# #遍歷圖片目錄集合
# for file in files:
#     #圖片的全路徑
#     filesname = dirs + '/' + file
#     #分割，為了儲存圖片檔案的格式和名稱
#     f = file.split('.')
#     #類似於建立檔案
#     datatmp = open(filesname, 'rb')
#     #建立寫入流
#     imgput = GridFS(mydb)
#     #將資料寫入，檔案型別和名稱通過前面的分割得到
#     insertimg=imgput.put(datatmp,content_type=f[1],filename=f[0])
#     datatmp.close()
# print("js")


#從MONGO抓照片
import pymongo
from pymongo import MongoClient
from gridfs import *

myclientdata = pymongo.MongoClient("mongodb+srv://")
mydbdata = myclientdata['test']
mycoldata = mydbdata['trash']

#給予girdfs模組來寫出，其中collection為上一步生成的，我不知道怎麼該名稱。實際上是由fs.flies和fs.chunks組成
gridFS = GridFS(mydbdata, collection="fs")
count=0
for grid_out in gridFS.find():
    count+=1
    print(count)
    data = grid_out.read() # 獲取圖片資料
    outf = open('%s.jpg'%(count),'wb')#建立檔案
    outf.write(data)  # 儲存圖片
    outf.close()
