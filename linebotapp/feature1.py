import pymongo
# myclient = pymongo.MongoClient("mongodb+srv://")
# mydb = myclient["test"]
# mycol = mydb["wow"]
# results = mycol.find({'Name': '又維'},{'_id':0})
# # print(results)
# for result in results:
#     print('名字:'+ result["Name"],'年齡:'+result["Age"])

# def getdata():
#     myclient = pymongo.MongoClient("mongodb+srv://")
#     mydb = myclient["test"]
#     mycol = mydb["wow"]
#     results = mycol.find({'Name': '又維'},{'_id':0})
#     # print(results)
#     for result in results:
#         # a = result["Name"]
#         # b = result["Age"]
#      print('名字:'+ result["Name"],'年齡:'+result["Age"])
# getdata()
# print('='*50)
# def test():
#     key = str(getdata())
#     return key
#
# test()
# print(type(test()))
#
# def getdata():
# id =5000
# Name = '又維'


myclient = pymongo.MongoClient("mongodb+srv://")
mydb = myclient['wow']
mycol = mydb['transaction']
results = mycol.find({}, sort=[('_id', -1)]).limit(1)
for result in results:
    print(result)
    # buy = '結帳成功，以下是您的清單\n' + result["Name"] + ' ' + '商品:' + \
    #     str(result["item_name"]) + ' ' + '數量:' + str(b) + ' ' + '金額:' + str(c)

# myclientdata = pymongo.MongoClient("mongodb+srv://")
# mydbdata = myclientdata['wow']
# mycoldata = mydbdata['transaction']
# results = mycoldata.find({})
# historys = []
# resultsbuy = mycoldata.find({}, sort=[('_id', -1)]).limit(1)
# for result in results:
#     date = str(result['date'])
#     Name = result['Name']
#     item = result['item']
#     Quantity = str(result['Quantity'])
#     price = str(result['price'])
#     # log = '以下是您的消費紀錄\n'
#     history = date+'\n'+'商品:'+item+' '+'數量:'+Quantity+' '+'金額:'+price+'\n'
#     historys.append(history)
#     # historys = ','.join(history)
# # print('+'*50)
# num = len(historys)
# strOut = ""
# for i in range(num):
#     d=historys[i]
#     strOut += d
#     print('='*50)
# data = strOut
# # print(data)
# # print(date+' '+'購買商品:'+item+' '+'數量:'+Quantity+' '+'金額:'+price)
# for resultbuy in resultsbuy:
#     Name = resultbuy['Name']
#     item = resultbuy['item']
#     Quantity = str(resultbuy['Quantity'])
#     price = str(resultbuy['price'])
#     buy = '結帳成功，以下是您的清單\n' + Name + ' ' + '商品:' + item + ' ' + '數量:' + Quantity + ' ' + '金額:' + price
#
# if 1>0:
#     print('='*50)
#     print((data))
#     # print((buy))