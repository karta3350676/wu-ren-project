from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)
from datetime import *
from linebot.models.template import *
from linebot.models import *
import requests
import datetime
import pymongo
#pip install dnspython
app = Flask(__name__)


# Channel Access Token
line_bot_api = LineBotApi('QuabeNVx6eWcz4UkF7WaqCymPAebcBgYpxStbtaR5JdIO9X2u1aB8uUux7aBOjXVPgppGhYRHmQiStE3eK1ZjuYY8Y/MeoZp27oSeKtNcY4ggHNPg7NmvZumPSnS48FiU9aec+exl31mkwiFx3+SqQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0c816c6dd4ba55fd253411058183b01b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID
    # line_bot_api.push_message(uid, message)
        # msg = msg.encoding('utf-8')

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
    # =====================     從 transaction table的id find 消費者的購物清單           ====================#
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
            allbuy.append(buy)
        num = len(allbuy)
        strOut = ""
        for i in range(num):
            d = allbuy[i]
            strOut += d
        buydata = strOut
        mycolback.insert_many([logout_data])  # 在logs狀態中增加會員登出的資料
    elif checkid != getid:  # 如果 id不相同 認定該消費者沒有購物
        Name = getid
        buydata = '謝謝光臨'
        mycolback.insert_many([logout_data])  #在logs狀態中增加會員登出的資料
        # mycol_getid.delete_one(deldata)       #登出時順便刪除在fit中登入的會員資料

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

    # if event.message.text == "結帳":
    #
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("HI~"+user_name+'\n'+buy))

    if event.message.text == "請稍後，正在為您處理":
        line_bot_api.reply_message(event.reply_token, TextSendMessage('以下是您的消費紀錄\n'+historydata))

    elif event.message.text == '1':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='111'))

    elif event.message.text == "廠商專區":
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title="HI~"+user_name+'廠商您好\n'+'請選擇以下您需要功能',
                text='                 請選擇以下功能',
                thumbnail_image_url='https://i.imgur.com/s1wqjHb.png',
                actions=[
                    URITemplateAction(
                        label='樞紐分析',
                        uri='https://pyhton-teach.herokuapp.com/wowpeople#'
                    ),
                    URITemplateAction(
                        label='會員購物傾向預測',
                        uri='https://elenalin.herokuapp.com/test'
                    ),
                    URITemplateAction(
                        label='AI動態系統',
                        uri='https://5449b24c5593.ngrok.io'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    elif event.message.text == "結帳":
        print("Confirm template")
        Confirm_template = TemplateSendMessage(
            alt_text='buy目錄',
            template=ConfirmTemplate(
                title='ConfirmTemplate',
                text="HI~"+user_name+'\n'+buydata,
                actions=[
                    PostbackTemplateAction(
                        label='購買結束',
                        text='謝謝光臨~~\n歡迎再次光臨',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='買得不夠爽',
                        text='請繼續參觀選購!!'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Confirm_template)

    elif event.message.text == "購物車":
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='您好~'+user_name,
                text='                 請選擇以下功能',
                thumbnail_image_url='https://i.imgur.com/s1wqjHb.png',
                actions=[
                    MessageTemplateAction(
                        label='結帳',
                        text='結帳'
                    ),
                    URITemplateAction(
                        label='幫你出主意',
                        uri='https://elenalin.herokuapp.com/test2'
                    ),
                    PostbackTemplateAction(
                        label='歷史紀錄',
                        text='請稍後，正在為您處理',
                        data='tr'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    elif event.message.text == "HI~"+ user_name+'\n'+'以下為您推薦這三款':
        print("Image Carousel")
        Image_Carousel = TemplateSendMessage(
            alt_text='Image Carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/VPgDKV7.jpg',
                        action=PostbackTemplateAction(
                            label='可樂',
                            text='可樂(330ml/罐) 20 元',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/8Z7EIX7.jpg',
                        action=PostbackTemplateAction(
                            label='富士蘋果',
                            text='富士蘋果(約50g/顆) 25 元',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MNKLPRN.jpg',
                        action=PostbackTemplateAction(
                            label='啤酒',
                            text='啤酒(330ml/罐) 30 元',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Image_Carousel)
        return 'OK2'
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)