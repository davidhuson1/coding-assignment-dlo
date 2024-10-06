from flask import Flask, render_template, request
import werkzeug.exceptions
from dlo import generateDloUrl
import os
import werkzeug

app = Flask(__name__)
app.config["BASE_URL"] = os.getenv("BASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_error(error):
    return render_template("error.html", error=error)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/getDLO")
def getDLO():
    userid = request.args.get("userid").strip()
    usertype = request.args.get("usertype")
    baseUrl = app.config["BASE_URL"]
    pathToOpen = request.args.get("pathToOpen")

    if not userid:
        return handle_error(
            {
                "code": 404,
                "title": "No user Id provided",
                "description": "Please provide an User ID",
            }
        )

    DloUrl = generateDloUrl(userid, usertype, baseUrl, pathToOpen)
    return render_template("getDLO.html", url=DloUrl, userid=userid, usertype=usertype)


if __name__ == "__main__":
    app.run()
