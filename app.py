from flask import Flask, render_template
from hogwarts import characters

app = Flask(__name__)

@app.route("/")
def index():
    message = {'title': 'Hello world'}
    return render_template('index.html')

@app.route("/characters/")
def chars():
    hogwarts = characters()
    return render_template('characters.html', chars=hogwarts)

@app.route("/students/")
def students():
    return render_template('students.html', title="Students from...")

if __name__ == '__main__':
    app.run(debug=False)