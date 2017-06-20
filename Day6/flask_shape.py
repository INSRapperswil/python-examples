from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/shape/<service_level>')
def hello(service_level=None):
    return render_template('shape.cfg', service_level=service_level)

if __name__ == '__main__':
    app.run()
    # http://127.0.0.1:5000/shape/S1
