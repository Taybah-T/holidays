from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def holiday():
    return holidays()

@app.route('/holiday', methods=["GET"])
def holidays():
    with open("holiday.json") as f:
        vacation =json.load(f)
        
    return render_template("holiday.html", data=vacation)

@app.post('/test')
def createTest():
    return "Success"

@app.get("/holiday")
def add_holiday():
    return render_template("holiday.html")

@app.get("/holiday/add")
def add():
    return render_template("add_holiday.html")

@app.post("/holiday")
def post_holiday():
    
    name=request.form["name"]
    start = request.form["start_date"]
    end = request.form["end_date"]
    
    with open("holiday.json") as f:
        adding = json.load(f)
        
    holidays.append({"name":name, "start_date":start, "end_date":end})


if __name__ == "__main__":
    app.run(debug=True)
    

