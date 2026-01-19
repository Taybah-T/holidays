import json 

with open("holiday.json") as f:
        holidays =json.load(f)
print(holidays)

with open('table.html') as f:
    html = f.read()
