from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Bitcoin!</p>"


@app.route("/wallet")
def get_wallet():
    return requests.get('https://developer.bitcoin.org/reference/rpc/getbalance.html').content