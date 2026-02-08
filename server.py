import json

app = FLask(__name__)

@app.get("/holiday")
#get list of holidays, shows the holidays already

@app.get("/holiday/add")
#add simple html form 
#add name of holiday, when it strats when it ends
#shows a form that adds the new holiday in when submit is clicked

#then triggers...

@app.post("/holiday")

#adds to the list of json holidays
#return all of holidays= new one that was made