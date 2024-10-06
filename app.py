from flask import Flask, render_template, request
from DLO import generateDloUrl

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/getDLO")
def getDLO():
    userid = request.args.get("userid")
    usertype = request.args.get("usertype")
    pathToOpen = request.args.get("pathToOpen")

    DloUrl = generateDloUrl(userid, usertype, pathToOpen)

    return render_template("getDLO.html", url=DloUrl, userid=userid, usertype=usertype)


if __name__ == "__main__":
    app.run()
