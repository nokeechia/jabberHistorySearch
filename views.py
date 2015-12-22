from app import app
from models import History_Message

from flask import render_template, request

@app.route('/')
def hello_world():
    messages = History_Message.query.all()
    print(History_Message.query.get(0))
    return render_template('index.html', messages=messages)

