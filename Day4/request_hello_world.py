import requests

r = requests.get('https://api.github.com/orgs/HSRNetwork')

print(r.text)
print(r.json())

r = requests.get('https://api.github.com/orgs/HSRNetwork')
print(r.text)
print(r.json())

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.text)
print(r.json())

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.text)
print(r.json())

r = requests.delete('http://httpbin.org/delete')
print(r.text)
print(r.json())


payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
print(r.text)
print(r.json())

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)
print(r.json())

r = requests.get('http://httpbin.org/get')
print(r.status_code)

print(r.status_code == requests.codes.ok)

print(r.headers)
