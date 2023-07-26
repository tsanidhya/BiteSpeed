from flask import Flask, request

from dto.identify.request import IdentifyRequest

app = Flask(__name__)
from dto.identify.response import IdentifyResponse
from config.db import PostgresConnect
from sqlalchemy import text
from model.Contact import Contact
postgres_db = PostgresConnect()
engine = postgres_db.engine

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/identify', methods=["POST"])
def identify(contactService=None):
    email = request.json['email']
    phoneNumber = request.json['phoneNumber']

    if not email and not phoneNumber:
        return "Email and phoneNumber cannot be both now", 400  # status return
    identify_request = IdentifyRequest(email, phoneNumber)
    return contactService.execute(identify_request), 200


if __name__ == "__main__":
    app.run(debug=True)