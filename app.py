from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data = {"message": "Hello"}
    return jsonify(data)

@app.post('/test')
def createTest():
    return "Success"


if __name__ == "main":
    app.run(debug=True)

