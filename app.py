from flask import Flask, request
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
def identify():
    email = request.json['email']
    phoneNumber = request.json['phoneNumber']

    print(email)
    print(phoneNumber)
    print("Done----------->")
    with engine.connect() as conn:
        response_db = conn.execute(text("select * from Contact;")).mappings().fetchall()
    print("response_db res-> ", response_db)
    for ele in response_db:
        model_val = Contact.from_response(ele)
        print("email yo: ",model_val.email)



    #dummy res
    return IdentifyResponse(
        primaryContatctId=5,
        emails= ["lorraine@hillvalley.edu", "mcfly@hillvalley.edu"],
        phoneNumbers= ["123456"],
        secondaryContactIds= [23]
    ).ret_json()


if __name__ == "__main__":
    app.run(debug=True)