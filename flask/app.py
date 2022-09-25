from flask import Flask
from db import database
from db.model import postal_code

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/postal-code")
def postal_code():
    conn = database.engine.connect()
    postal_code_model = postal_code(conn)
    address = postal_code_model.search_address_by_postal_code('5270205')

    return address
