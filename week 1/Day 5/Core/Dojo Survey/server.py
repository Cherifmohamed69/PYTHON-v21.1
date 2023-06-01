from flask import Flask,render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/process', methods=["POST"])
def process():
    session['Name']=request.form['Name']
    session['Location']=request.form['Location']
    session['Language']=request.form['Language']
    session['comment']=request.form['comment']
    return redirect("/result")

@app.route('/result')
def create_user():

 return render_template("display.html",name=session['Name'],location=session['Language']
,Language=session['Language'],comment=session['comment'])


if __name__ == '__main__':
    app.run(debug=True)