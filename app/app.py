from flask import Flask, json
import socket, os

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<body style='background-color:{os.environ.get('BG_COLOR')};'>\
    <h1 style='color:{os.environ.get('FONT_COLOR')}'>{os.environ.get('CUSTOM_HEADER')}</h1> \
    <img src='{os.environ.get('CUSTOM_PHOTO')}' alt='CUSTOMER_PHOTO'>\
    <h2 style='color:{os.environ.get('FONT_COLOR')};'>Hello World! Served from <b>{socket.gethostname()}</b></h2></body>"
    return html