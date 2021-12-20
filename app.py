from flask import Flask, render_template
import hogwarts

app = Flask(__name__)

@app.route("/")
def index():
    message = {'title': 'Hello world'}
    return render_template('index.html')

@app.route("/characters/")
def chars():
    return render_template('characters.html', chars=hogwarts.characters())

@app.route("/students/")
def students():
    return render_template('students.html', title="Students from...")

@app.route('/students/<house>/')
def chars_by_house(house):
    students_by_house = hogwarts.characters_classified(house)
    return render_template('students-by-house.html', context=students_by_house, house=house)

@app.route('/staff/')
def hogwarts_staff():
    staff = hogwarts.staff()
    return render_template('staff.html', context=staff)

@app.route('/<name>/')
def character(name):
    chars = hogwarts.characters()
    context = next(char for char in chars if char['name'] == name)
    return render_template('character.html', context=context)

@app.route('/houses')
def houses():
    return render_template('houses.html')

@app.route('/houses/<house_name>')
def house(house_name):
    return render_template('house.html', house=house_name)

if __name__ == '__main__':
    app.run(debug=True)