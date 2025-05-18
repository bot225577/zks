
from flask import Flask, request

app = Flask(__name__)

@app.route("/twitter-webhook", methods=["POST"])
def twitter_webhook():
    data = request.get_json()
    print("📥 收到推文：", data)
    return '', 200
