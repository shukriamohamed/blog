from unicodedata import name
from flask import Flask, render_template, url_for
app = Flask(__name__) 


@app.route("/")
@app.route("/index")                         
def index():                                    
    return render_template('index.html') 


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)

if __name__ == '__main__':
    app.run(debug=True)
