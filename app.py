from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def holiday():
    return holidays()

@app.route('/holiday', methods=["GET"])
def holidays():
    with open("holiday.json") as f:
        data =json.load(f)
        
    return render_template("holidays.html", holidays=holidays)

    return jsonify(data)

@app.post('/test')
def createTest():
    return "Success"


if __name__ == "__main__":
    app.run(debug=True)

