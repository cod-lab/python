from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='temp')

@app.route('/index')
def msg1():
    return "<h1>welcome brooooooooo </h1> <input type = 'submit' class = 'close' caption = 'close'> "

@app.route('/contact')
def msg2():
    return "contact us"

@app.route('/<name>')
def msg3(name):
    return "hey "+name

@app.route('/myapp')
def msg4():
    return render_template('myapp.html')

if __name__ == '__main__':
    app.run()

