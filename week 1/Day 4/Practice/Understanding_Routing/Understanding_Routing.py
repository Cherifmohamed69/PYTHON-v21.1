from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/Dojo!')          # The "@" decorator associates this route with the function immediately following
def hello():
    return 'Dojo!!'  # Return the string 'Hello World!' as a response



@app.route('/say/<flask>')
def hi_Flask(flask):
    return 'Hi'+ ' ' + flask


@app.route('/say/<michael>')
def hi_Michael(Michael):
    return 'Hi'+ ' ' + Michael


@app.route('/say/<John>')
def hi_John(John):
    return 'Hi'+ ' ' + John


@app.route('/test/<text>/<int:num>')
def repeat(text,num):
    word=""
    for i in range(0,num):
        word+=f'hello,{text} <br>'
        
       
    return word



@app.route('/repeat/<path:path>')
def repeat_word(path):

    return 'sorry no file no path!'






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)