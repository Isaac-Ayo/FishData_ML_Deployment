import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'species':0, 'length1':23.2, 'length2':25.4, 'length3':30.0, 'height':11.5200, 'width':4.0200})

print(r.json())