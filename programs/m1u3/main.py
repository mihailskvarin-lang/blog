from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    file = open('C:/programs/m1u3/index.html', "r", encoding="utf-8")
    code = file.read()
    return code

@app.route("/blog1")
def first_post():
    return render_template('1post.html')

@app.route("/blog2")
def second_post():
    return render_template('2post.html')

@app.route("/blog3")    
def third_post():
    return render_template('3post.html')

@app.route("/blog4")
def fourth_post():
    return render_template('4post.html')

@app.route("/about")    
def about():
    return render_template('about.html')

app.run(debug=True)