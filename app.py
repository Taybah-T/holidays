from flask import Flask, jsonify, render_template, request, redirect, url_for
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



@app.get("/holiday/add")
def add():
    return render_template("add_holiday.html")

@app.post("/holiday")
def post_holiday():
    
    name=request.form["name"]
    start = request.form["start_date"]
    end = request.form["end_date"]
    
    with open("holiday.json") as f:
        holidays = json.load(f)
        
    holidays.append({"name":name, "start_date":start, "end_date":end})
    

    with open("holiday.json",'w') as f:
        json.dump(holidays,f,indent=4)

    return redirect(url_for("holiday"))

if __name__ == "__main__":
    app.run(debug=True)
    

