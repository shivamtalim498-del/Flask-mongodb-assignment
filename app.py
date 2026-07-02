from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://shivamtalim498_db_user:HmH8Ree8YY96yccN@cluster0.rplgp1k.mongodb.net/?appName=Cluster0")
db = client["studentdb"]
collection = db["students"]


# ---------------- API Route ----------------
@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)


# ---------------- Home Page ----------------
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect("/success")

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")


# ---------------- Success Page ----------------
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)