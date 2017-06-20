from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/print')
def print():
    name = request.args.get('name')
    favorite_pizza = request.args.get('favorite_pizza')
    return '{name} likes {pizza}'.format(name=name, pizza=favorite_pizza)

if __name__ == '__main__':
    app.run()
    # http://127.0.0.1:5000/print?favorite_pizza=dieci&name=sepp
