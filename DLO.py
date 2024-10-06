import uuid
from dotenv import load_dotenv
from pprint import pprint
import urllib.parse
import os
import datetime
import hashlib
import hmac

load_dotenv()
secret = os.getenv("DLO_SECRET")
baseUrl = os.getenv("BASE_URL")


def generateToken(message, secret):
    if not message or not secret:
        raise ValueError("'message' or 'secret' cannot be empty")

    token = hmac.new(
        secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha512
    ).hexdigest()

    return token


def generateDloUrl(userid, usertype, baseUrl, pathToOpen):
    if not userid or not usertype or not baseUrl:
        raise ValueError("'Userid' or 'usertype' cannot be empty")

    formattedTimestamp = datetime.datetime.now().isoformat() + "+02:00"
    nonce = str(uuid.uuid4())

    message = (
        "nonce"
        + nonce
        + "timestamp"
        + formattedTimestamp
        + "userid"
        + userid
        + "usertype"
        + usertype
    )

    token = generateToken(message, secret)

    params = {
        "usertype": usertype,
        "userid": userid,
        "nonce": nonce,
        "timestamp": formattedTimestamp,
        "token": token,
    }

    DloUrl = baseUrl + pathToOpen + "?" + urllib.parse.urlencode(params)
    return DloUrl


if __name__ == "__main__":
    print("\n *** Generate DLO URL: ***")

    userid = input("\nPlease enter a userid: ")
    usertype = input("\nPlease enter a usertype: ")
    pathToOpen = input("\nPlease enter a path to open (optional): ")

    DloUrl = generateDloUrl(userid, usertype, baseUrl, pathToOpen)

    print("\nDLO URL is:")
    pprint(DloUrl)
