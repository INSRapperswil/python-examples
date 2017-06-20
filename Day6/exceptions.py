try:
    data = ['spam', 'eggs', 'bacon']
    print(data[100])
except IndexError as e:
    print('You accessed an invalid index')
    print(e)

try:
    data = {'bacon': 'backed'}
    print(data['eggs'])
except KeyError as e:
    print(e)

import requests
from requests.exceptions import ConnectionError, Timeout

try:
    requests.get('http://www.nettowel.ch')
    print('All fine')
except ConnectionError:
    print('Maybe DNS Error or refused connection')

except Timeout:
    print('Server didn’t answer on time')


class MyError(Exception):
    pass

try:
    raise MyError()
except MyError:
    print('Got a MyError exception')