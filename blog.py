from flask import Flask, render_template, url_for
app = Flask(__name__) 


@app.route("/")
@app.route("/home")                         
def home():                                    
    return 'Hello shukri'
    #render_template('home.html',posts=posts) 


@app.route("/about")
def about():
    return 'Hi There'
    #render_template('about.html', title='About') #want title here

if __name__ == '__main__':
    app.run(debug=True)
