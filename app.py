from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Example user
users = {
    "admin@example.com": generate_password_hash("Password123")
}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    if email in users and check_password_hash(users[email], password):
        return redirect("/dashboard")

    return "Invalid email or password"

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome!</h1>"

if __name__ == "__main__":
    app.run(debug=True)