from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''<html>
                <body>
                <form action="/print" method="post">
                  Name: <input type="text" name="name"> <br>
                  Favorite Pizza: <input type="text" name="favorite_pizza"><br>
                  <input type="submit" value="Submit">
                </form>
                </body>
              </html>'''


@app.route('/print', methods=['POST'])
def print():
    name = request.form['name']
    favorite_pizza = request.form['favorite_pizza']
    return '{name} likes {pizza}'.format(name=name, pizza=favorite_pizza)


if __name__ == '__main__':
    app.run()
