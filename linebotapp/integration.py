import pymongo

# =====================    在 logs tables 找進入商店的id           ====================#
# 導入pymongo
client_getid = pymongo.MongoClient(
    "mongodb+srv://")
# mongo固定ip位置
mydb_getid = client_getid['wow']   #db name
mycol_getid = mydb_getid['members']    #tables name
results_getid = mycol_getid.find({}, sort=[('_id', -1)]).limit(1)
for result_getid in results_getid:
    getid = result_getid["id"]
    # status = result_getid["status"]
    # print(status)
    # if status == 'in' and status == 'out':
    #     print('yes')
    # else:
    #     print('no')
    # =====================     從 wow tables的id find 消費者的購物 id          ====================#
    myclient_checkid = pymongo.MongoClient(
        "mongodb+srv://")
    mydb_checkid = myclient_checkid["mydatabase"]
    mycol_checkid = mydb_checkid["items"]
    results_checkid = mycol_checkid.find({}, sort=[('_id', -1)]).limit(1)
    for result_checkid in results_checkid:
        checkid = result_checkid["item_id"]
        # status = result_getid["status"]
        # print(result_checkid)
        # =====================     從 logs tables的id find 消費者的購物清單           ====================#
        if checkid == getid:    # 確定在登入及購物兩個tables 都有相同id 才執行消費清單
            id = checkid
            myclientbuy = pymongo.MongoClient("mongodb+srv://")
            mydbbuy = myclientbuy["wow"]
            mycolbuy = mydbbuy["members"]
            myclient2 = pymongo.MongoClient(
                "mongodb+srv://")
            mydb2 = myclient2["mydatabase"]
            mycolbuy2 = mydb2["items"]
            resultsbuy2 = mycolbuy2.find({'item_id': id},sort=[('_id', -1)]).limit(1)
            resultsbuy = mycolbuy.find({'id': id},sort=[('_id', -1)]).limit(1)
            # results2 = mycol2.find()
            # results = mycol2.find()
            for resultbuy2 in resultsbuy2:
                # print(resultbuy2)
                nums = mycolbuy2.aggregate([{'$count': 'num of item_id'}])
                a = 3
                for num in nums:
                    b = a - num['num of item_id']
                    if b == 1:
                        c = 10
                    elif b == 2:
                        c = 20
                    elif b == 3:
                        c = 30
                    # print(a - num['num of item_id'])
                    for resultbuy in resultsbuy:
                        # a = resultbuy["Age"]
                        # b = '已購買:' + str(resultbuy["item"])
                        # c = '金額:'+ str(resultbuy["price"])
                        # d = a+ ' ' + b+ ' ' +c
                        # print(a)
                        # print(2,resultbuy)
                        d = '結帳成功，以下是您的清單\n' + resultbuy["Name"] + ' ' + '商品:' +\
                            str(resultbuy2["item_name"]) + ' ' + '數量:' + str(b) + ' '+'金額:'+ str(c)
                        # print(d)
        elif checkid != getid:   # 如果 id不相同 認定該消費者沒有購物
            d = '謝謝光臨'
            # print(d)

    if 1>0:
        print(d)




# myclient = pymongo.MongoClient("mongodb+srv://")
# mydb = myclient["mydatabase"]
# mycol = mydb["items"]
# results = mycol.find({},{'_id':0})
# for result in results:
#     print(result)
# nums = mycol.aggregate([{'$count': 'num of item_id'}])
# a =3
# for num in nums:
#     b = a - num['num of item_id']
#     if b == 0:
#         d = 'aaaa'
#     elif b == 1:
#         d = 10
#     elif b == 2:
#         c = 20
#     elif b == 3:
#         c = 30
#     print(d)