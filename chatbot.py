from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("responses.json") as file:
    responses = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.form["msg"].lower()
    reply = responses.get(user_input, "Sorry, I don't understand that.")
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
