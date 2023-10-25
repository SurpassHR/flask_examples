from flask import Flask, render_template, request
from stub_ssh_response import StubBoardResponse, BoardCmd
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

@app.route("/shell_ping", methods = ['GET'])
def ShellPing():
    ret = StubBoardResponse(hostip="10.91.15.208", cmd=BoardCmd.SHELL_PING)
    respList = ret.split("\n")
    for i in range(len(respList)):
        if respList[i] == "":
            respList.remove(respList[i])

    for item in respList:
        print(item)
    return respList
