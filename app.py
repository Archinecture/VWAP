from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["GET"])
def callback():
    auth_code = request.args.get("code")
    if auth_code:
        return f"Authorization code received: {auth_code}"
    else:
        return "No authorization code found", 400

if __name__ == "__main__":
    app.run()
