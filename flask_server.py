from flask import Flask
import json
import subprocess

app = Flask(__name__)

def get_balance():
    return json.loads(subprocess.check_output(["bitcoin-cli", "-conf=/home/testnet/bitcoin.conf", "getbalances"]))

@app.route("/")
def hello_world():
    balance = get_balance()
    confirmed = balance["mine"]["trusted"]
    unconfirmed = balance["mine"]["untrusted_pending"]
    return "<h2>Zbieram na czesne tb1qgj5x6kw7a6dsx87fl5ysrfrnzxz3uj0pcp9ekm</h2><p>" + str(confirmed) + " " + str(unconfirmed) + "</p>"