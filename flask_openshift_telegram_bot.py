from bot import Bot
from flask import Flask, abort, jsonify, request
from settings import TELEGRAM_SECRET_URL

app = Flask(__name__)


@app.route("/")
def index():
    response = {"status": "OK"}
    return jsonify(**response)


@app.route("/<secret_url>", methods=["POST"])
def login(secret_url):
    if not TELEGRAM_SECRET_URL == secret_url:
        abort(404)
    payload = request.get_json()
    if not Bot.valid_payload(payload):
        abort(400)
    chat_id = payload["message"]["chat"]["id"]
    text = payload["message"]["text"]
    response = Bot.process_message(chat_id, text)
    return jsonify(**response)


if __name__ == '__main__':
    app.run()
