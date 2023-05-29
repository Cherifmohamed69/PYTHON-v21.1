from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"






@app.route('/')      
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    print (session)
    return render_template ('index.html')


@app.route('/guess',methods=['POST'])
def guess():
        session['guess'] = int(request.form['guess'])
        
        return render_template ('index.html')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

















if __name__=="__main__":   
    app.run(debug=True) 