from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask App is Running! Go to /login to authenticate."

@app.route("/login")
def login():
    """Redirect user to Schwab's OAuth login page."""
    auth_url = (
        f"https://api.schwabapi.com/v1/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=read_accounts read_positions read_transactions trade execute"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    """Handle OAuth callback and exchange code for access token."""
    auth_code = request.args.get("code")
    if not auth_code:
        return "❌ Error: Authorization code not found.", 400
    return f"✅ Authorization Code: {auth_code}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
