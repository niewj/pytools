import flask
from flask.app import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def showUserName(name):
    return '<h1> You Are %s</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
