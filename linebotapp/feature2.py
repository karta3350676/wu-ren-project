import pymongo
import datetime


client = pymongo.MongoClient(
        "mongodb+srv://")
# mongo固定ip位置
mydb = client['wow']  # db name
mycol_getid = mydb['fit']  # tables name
mycol_checkid = mydb["transaction"]
mydbback = client['wow']  # db name
mycolback = mydbback['logs']  # tables name

results_getid = mycol_getid.find({}, sort=[('_id', -1)]).limit(1)
for result_getid in results_getid:
    getid = result_getid["Name"]
    # print(result_getid)

results_checkid = mycol_checkid.find({}, sort=[('_id', -1)]).limit(1)
for result_checkid in results_checkid:
    checkid = result_checkid["Name"]
    # print(2, result_checkid)
    datetime_dt = datetime.datetime.today()  # 獲得當地時間
    time_delta = datetime.timedelta(hours=8)  # 時差
    new_dt = datetime_dt + time_delta  # 本地時間加8小時
    datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期(最小單位到秒)
    Name = getid
    deldata = {"Name": Name}
    logout_data = {
        "id": '',
        "Name": checkid,
        "type": 'logout',
        "Time": datetime_format
    }
# =====================     從 logs tables的id find 消費者的購物清單           ====================#
if checkid == getid:  # 確定在登入及購物兩個tables 都有相同id 才執行消費清單
    Name = getid
    historys = []
    resultshistory = mycol_checkid.find({"Name": Name})
    for resulthistory in resultshistory:
        all = str(resulthistory).split(',')  # 把json 轉字 #split用 , 分割
        # print(all)
        times = all[1].replace("'", '').strip()  # 把 ' 取代空字串 strip()刪除前後空白字元
        time = times[7:]
        # print(time)

        names = all[2].replace("'", '')  # 把 ' 取代空字串
        name = names[7:]

        items = all[3:]
        item = str(items).replace("'", '').replace('"', '').replace('}', '') \
            .replace(',  ', '\n').strip('[]').strip().replace('商品1', '商品').replace('商品2', '商品').replace('商品3', '商品')
        history = times + '\n' + name + '\n' + item + '\n'
        # print(history)
        historys.append(history)
    num = len(historys)
    strOut = ""
    for i in range(num):
        d = historys[i]
        strOut += d
    historydata = strOut

elif checkid != getid:  # 如果 id不相同 認定該消費者沒有購物
    historydata = '抱歉您無任何購買紀錄'



if checkid == getid:  # 確定在登入及購物兩個tables 都有相同id 才執行消費清單
    Name = getid
    allbuy = []
    resultsbuy = mycol_checkid.find({"Name": Name}, sort=[('_id', -1)]).limit(1)
    for resultbuy in resultsbuy:
        all = str(resultbuy).split(',')  # 把json 轉字 #split用 , 分割

        times = all[1].replace("'", '')  # 把 ' 取代空字串
        time = times[7:]

        names = all[2].replace("'", '')  # 把 ' 取代空字串
        name = names[7:]

        items = all[3:]
        item = str(items).replace("'", '').replace('"', '').replace('}', '') \
            .replace(',  ', '\n').strip('[]').strip().replace('商品1', '商品').replace('商品2', '商品').replace('商品3', '商品')
        buy = '結帳成功，以下是您的清單\n' + name + '\n' + item + '\n'
        # print(ee)
        allbuy.append(buy)
    num = len(allbuy)
    strOut = ""
    for i in range(num):
        d = allbuy[i]
        strOut += d
        # print('=' * 50)
    buydata = strOut
    mycolback.insert_many([logout_data])
    mycol_getid.delete_one(deldata)
    # print(data)
elif checkid != getid:  # 如果 id不相同 認定該消費者沒有購物
    Name = getid
    buydata = '謝謝光臨'
    mycolback.insert_many([logout_data])
    mycol_getid.delete_one(deldata)



#
if 1>0:
    # print(Name)
    # print(buydata)
    print(logout_data)
    print('='*50)
    print('以下是您的消費紀錄\n' + historydata)





    # try:
    #     if a[4] != None :
    #         c = a[3].replace("'", '').replace('}', '')
    #         d = a[4].replace("'",'').replace('}','')
    #         d= d.replace(d[4], "")  #將 商品2: 轉成 商品:
    #         # print(bb)    #第3個字,空字串
    #         # print(c)
    #         # print(d)
    #     elif a[3] != None:
    #             c = a[3].replace("'", '').replace('}', '')
    #             # print(bb)
    #             # print(c)
    #     else:
    #         e = '謝謝光臨'
    # except:
    #     pass
        # print('vvv')
        # if 1>0:
        #     # print('='*50)
        #     print(bb)
        #     print(c)
        #     print(d)
        #     print(e)

# client_checkid = pymongo.MongoClient(
#     "mongodb+srv://")
#
# mydb_checkid = client_checkid.test
# mycol_checkid = mydb_checkid['wow']
# results_checkid = mycol_checkid.find({}, sort=[('_id', -1)]).limit(1)
# for result_checkid in results_checkid:
#     checkid = result_checkid["id"]
#     # status = result_getid["status"]
#     print(result_checkid)