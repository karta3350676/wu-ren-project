from flask import Flask
teach=Flask(__name__, static_url_path='/static',static_folder='./static') # __name__ 代表目前執行的模組

from flask import render_template
@teach.route("/test")
def home():
    return render_template("test.html")

@teach.route("/project")
def home2():
    return render_template("index2.html")

if __name__=="__main__": # 如果以主程式執行
    teach.run() # 立刻啟動伺服器