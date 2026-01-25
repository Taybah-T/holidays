import json 
import webbrowser

def json_to_html():
    with open("holiday.json") as f:
            holidays =json.load(f)
    print(holidays)

    json_j = json.dumps(holidays)

    html = f"<html><body><pre>{json_j}</pre></body></html>"

    with open('table.html', 'w') as f:
        f.write(html)
        
    webbrowser.open("table.html")

    return "success"
json_to_html()
