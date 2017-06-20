from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
    # http://127.0.0.1:5000/hello/sepp
    # http://127.0.0.1:5000/hello
