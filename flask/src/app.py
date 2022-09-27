from flask import Flask
from db import database
from db.model.postal_code import PostalCode

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/postal-code")
def postal_code():
    conn = database.engine.connect()
    postal_code_model = PostalCode(conn)
    rows = postal_code_model.search_address_by_postal_code('5270205')

    address = []
    for row in rows:
        buff = {}
        for field in row._fields:
            buff[field] = row._mapping[field]
        address.append(buff)

    return address

@app.route("/postal-code2")
def postal_code2():
    conn = database.engine.connect()
    postal_code_model = PostalCode(conn)
    rows = postal_code_model.search_address_by_postal_code2('5270205')

    address = []
    for row in rows:
        buff = {}
        for field in row._fields:
            buff[field] = row._mapping[field]
        address.append(buff)

    return address
