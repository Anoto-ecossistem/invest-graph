from flask import Flask, render_template
import requests

url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=YAKKXBYH26HZ14CD'
r = requests.get(url)
data = r.json()

print(data)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html') 