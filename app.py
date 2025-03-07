from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    print("Received:", data)
    return "Success", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
