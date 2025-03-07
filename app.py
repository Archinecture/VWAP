from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json  # Receive JSON data from Schwab API
    print("Received:", data)  # Log the data
    return "Success", 200  # Send success response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
