from flask import Flask, render_template, request
from stub_ssh_response import StubBoardResponse
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods = ["POST"])
def post():
    textarea_data = request.form["textarea_data"];
    if len(textarea_data) == 0:
        print("no data posted")
    print(textarea_data)
    return "fuck"

@app.route("/get", methods = ['GET'])
def get():
    list = ['haha', 'hehe', '李雨点傻蛋']
    listJson = json.dumps(list)
    return listJson
