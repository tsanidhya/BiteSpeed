from flask import Flask
from router.ContactController import contact_blueprint
app = Flask(__name__)
app.register_blueprint(contact_blueprint)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

if __name__ == "__main__":
    app.run(debug=True)