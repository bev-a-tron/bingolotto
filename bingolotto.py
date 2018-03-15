from flask import Flask,render_template,request,redirect
import random

app = Flask(__name__)
NUMBERS = [1, 3, 13, 16, 22, 28, 30, 38, 39, 40, 43, 45, 46, 47, 55, 57, 59, 61, 64, 70, 72, 73, 75]

@app.route('/index',methods=['GET','POST'])
def index():
    random.shuffle(NUMBERS)
    number = NUMBERS.pop()
    if number <= 15:
        letter = 'B'
    elif number > 15 and number <= 30:
        letter = 'I'
    elif number > 30 and number <= 45:
        letter = 'N'
    elif number > 45 and number <= 60:
        letter = 'G'
    else:
        letter = 'O'
    
    return render_template('main.html',number=letter + str(number))

if __name__ == "__main__":
    app.run()
