from flask import Flask
from db import database
from db.model.postal_code import PostalCode

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/postal-code1")
def postal_code1():
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

@app.route("/postal-code-total")
def postal_code3():
    conn = database.engine.connect()
    postal_code_model = PostalCode(conn)
    prefectures = ["北海道", "青森県", "岩手県", "秋田県", "宮城県", "山形県", "大阪府", "東京都", "京都府", "愛知県", "島根県"]
    rows = postal_code_model.search_address_by_prefectures(prefectures)

    total = 0
    for row in rows:
        total = total + int(row['postal_code'])

    return {"total": total}
