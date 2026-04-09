import requests

r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json', 'User-Agent': 'My Library (https://github.com/phadeline/Joke)'})

print(r.json()['joke']);