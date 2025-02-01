from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)
def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    include_uppercase = 'uppercase' in request.form
    include_numbers = 'numbers' in request.form
    include_special = 'special' in request.form
    password = generate_password(length, include_uppercase, include_numbers, include_special)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)