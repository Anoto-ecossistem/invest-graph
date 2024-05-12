from flask import Flask
import requests

url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=YAKKXBYH26HZ14CD'
r = requests.get(url)
data = r.json()

print(data)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, project invest graph</p>"