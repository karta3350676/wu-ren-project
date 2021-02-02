from pymongo import MongoClient
import urllib.parse


import pymongo

import datetime



datetime_dt = datetime.datetime.today() # 獲得當地時間
time_delta = datetime.timedelta(hours=8) #時差
new_dt = datetime_dt + time_delta #本地時間加8小時
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期(最小單位到秒)

# member = {
#             'Time': datetime_format,
#             'Name': '臭鮑魚',
#             '商品': '跳蛋  數量: 3 價格: 90',
#             '商品2': '按摩棒  數量: 3 價格: 90'
#         }
member = {
    # "id":2518,
            "Name": 'Elsie',
    # "type":'logout',
    # "Time": datetime_format

        }
# Elsie
# Elena
client = pymongo.MongoClient(
    "mongodb+srv://")

mydb = client.wow
mycol = mydb['fit']
mycol.insert_many([member])  #新增
# mycol.delete_many({'Name': 'Elena'})  #刪除全部
# mydb = myclient.wow
# mycol = mydb["transaction"]
# mycol = mydb["members"]
# transation 資料為交易紀錄logs members  資料為辨識人員logs


# transaction
myclientdata = pymongo.MongoClient("mongodb+srv://")
mydbdata = myclientdata['wow']
mycoldata = mydbdata['fit']
results = mycoldata.find({})
historys = []
resultsbuy = mycoldata.find({}, sort=[('_id', -1)]).limit(1)
for result in results:
    print(result)
