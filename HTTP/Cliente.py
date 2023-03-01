import requests

r = requests.get('http://127.0.0.1:8000/example')
print(r.text)

requests.post('http://127.0.0.1:8000',data = 'texto')