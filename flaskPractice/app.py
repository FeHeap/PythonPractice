from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


#路由解析，通過用戶訪問的路徑，匹配相應的函數
@app.route('/HelloWorld')
def hello_world():
    return 'Hello World!'

#debug模式開啟

@app.route("/index1")
def index1():
    return '你好'

#通過訪問路徑，獲取用戶的字符串參數
@app.route("/user/<name>")
def welcome(name):
    return '你好,%s'%name

#通過訪問路徑，獲取用戶的整形參數               此外，還有float類型
@app.route("/user/<int:id>")
def welcome2(id):
    return '你好,%d號的會員'%id

#路由路徑不能重複，僅能透過唯一路徑訪問特定函數

#返回給用戶渲染後的網頁文件
@app.route("/index2")
def index2():
    return render_template("index2.html")

#向頁面傳遞一個變量
@app.route("/")
def index3():
    time = datetime.date.today()    #普通變量
    name = ["Fe","Luder","Suisei"]  #列表類型
    task = {"任務":"打掃衛生","時間":"3小時"} #字典類型
    return render_template("index3.html",var = time,list = name,task = task)

#表單提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")

#接收表單提交的路由，需要指定methods為POST
@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html",result=result)


if __name__ == '__main__':
    app.run()
