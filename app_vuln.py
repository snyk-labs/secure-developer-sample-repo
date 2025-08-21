from flask import request
import os

def vulnerable():
    # Hardcoded secret
    password = "hunter2"

    # Command injection (Snyk Code will flag)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
