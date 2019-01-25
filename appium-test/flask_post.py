from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'hongnaiwu' and password == 'naiwu3425':
            return "<h1>welcome , %s !</h1>" %username
        else:
            return "<h1>login failed !</h1>"
    else:
        return "<h1>login failure !</h1>"

if __name__ == '__main__':
    app.run(debug=True)