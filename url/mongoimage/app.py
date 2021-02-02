import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import pymongo



UPLOAD_FOLDER = './img'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__, template_folder='./')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html', template_folder='./')
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                   filename))
            filenames.append(filename)

    if request.method == 'GET':
        print("ok")
    elif request.method == 'POST':
        member_name = request.form.get("member_name")
        member_age = request.form.get("member_age")
        member_email = request.form.get("member_email")
        member_maritalstatus = request.form.get("member_maritalstatus")
        member_income = request.form.get("member_income")
        number = request.form.get("number")
        kid = request.form.get("kid")

        member = {
            "Name": member_name,
            "Age": member_age,
            "Email": member_email,
            "Marriage": member_maritalstatus,
            "Income": member_income,
            "Family": number,
            "Kid": kid
        }
        client = pymongo.MongoClient(
            "mongodb+srv://peter:0987602620@cluster0.0qqo9.mongodb.net/ceb101?retryWrites=true&w=majority")

        mydb = client.test
        mycol = mydb['trash']
        mycol.insert_many([member])  # 新增


    return   """
        <html>
        <head>
            <title>會員資料</title>
        <head>
        <body>
            <center><h1>加入會員成功</h1></center>
        </body>
        """


if __name__ == '__main__':
    app.run(debug=True)