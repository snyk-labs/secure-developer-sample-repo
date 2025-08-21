from flask import Flask, request
import subprocess, yaml, requests

app = Flask(__name__)

API_KEY = "sk_test_12345"  # hardcoded secret (Snyk Code will flag)

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Vulnerable: command injection via shell=True
    out = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return out

@app.route("/upload", methods=["POST"])
def upload():
    # Vulnerable: unsafe YAML load
    data = yaml.load(request.data, Loader=None)
    return {"ok": True, "data": str(data)}

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "http://example.com")
    # Bad practice: verify=False
    r = requests.get(url, verify=False)
    return r.text

if __name__ == "__main__":
    app.run(debug=True)
