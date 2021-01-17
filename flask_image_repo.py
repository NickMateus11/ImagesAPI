import requests
from flask import Flask
import json

app = Flask(__name__)
API_KEY = '563492ad6f91700001000001b468a1cff0e34319b5287f382e03b2e1'


@app.route('/')
def home():
    endpoint = 'search'
    res = requests.get(
        f'https://api.pexels.com/v1/{endpoint}', 
        params={'query': 'elephant'}, 
        headers={'Authorization': API_KEY}
    )

    if res.ok:
        return res.json()
    else:
        print(res)
        return "Error"


app.run(debug=True)