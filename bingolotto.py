

from flask import Flask,render_template,request,redirect
app = Flask(__name__)
NUMBERS = [1, 3, 13, 16, 22, 28, 30, 38, 39, 40, 43, 45, 46, 47, 55, 57, 59, 61, 64, 70, 72, 73, 75]

@app.route('/index',methods=['GET','POST'])
def index():
    number = NUMBERS.pop()
    return render_template('main.html',number=number)

if __name__ == "__main__":
    app.run()
