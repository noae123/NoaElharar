from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

#root of our website
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/templates/home.html')
def home():
    return render_template('home.html')

@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

    