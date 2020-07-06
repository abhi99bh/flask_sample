from flask import Flask,redirect,url_for,request,render_template
#from rasa.nlu.model import Interpreter

#NLU_Interpreter = Interpreter.load("//Users/abhi/Documents/bot/Corona_Analysis/chatbot/models/model/nlu")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    #msg = NLU_Interpreter.parse(name)['intent']
    msg = 'Sucess'
    return msg 

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for('success', name =user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))



if __name__ == '__main__':
    app.run("0.0.0.0", port=5001, debug=True)