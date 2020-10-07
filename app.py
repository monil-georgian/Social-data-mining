from flask import Flask, render_template,request,redirect,url_for
from bson import ObjectId # For ObjectId to work    
import pymongo
from pymongo import MongoClient    
import os   

app = Flask(__name__) 

client = pymongo.MongoClient("mongodb+srv://boardgames:boardgames@social-data-mining.ashep.azure.mongodb.net/boardgames?retryWrites=true&w=majority")
db = client.boardgames #Select the database
boardgames = db.boardgames #Select the collection name

#redirect page to index page
def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list")    
def lists ():    
    #Display the all Board Games    
    allBoardgames = boardgames.find()
    a1="active"      
    return render_template('list.html',a1=a1,boardgames=allBoardgames)    
  
@app.route("/action", methods=['POST'])    
def action ():    
    #Adding a Board Game    
    name=request.values.get("name")
    image_url=request.values.get("image_url")    
    min_players=request.values.get("min_players")    
    max_players=request.values.get("max_players")    
    min_playtime=request.values.get("min_playtime")
    max_playtime=request.values.get("max_playtime")
    min_age=request.values.get("min_age")    
    boardgames.insert({ "name":name, "image_url":image_url, "min_players":min_players, "max_players":max_players, "min_playtime":min_playtime, "max_playtime":max_playtime, "min_age":min_age})    
    return redirect("/list")    
  
@app.route("/remove")    
def remove ():    
    #Deleting a Task with various references    
    key=request.values.get("_id")    
    boardgames.delete_one({"_id":ObjectId(key)})    
    return redirect("/list")    
  
@app.route("/update")    
def update ():    
    id=request.values.get("_id")    
    boardgame=boardgames.find({"_id":ObjectId(id)})    
    return render_template('update.html',boardgames=boardgame)

@app.route("/view")    
def view ():    
    id=request.values.get("_id")    
    boardgame=boardgames.find({"_id":ObjectId(id)})    
    return render_template('view.html',boardgames=boardgame)    
  
@app.route("/action3", methods=['POST'])    
def action3 ():    
    #Updating a Task with various references    
    name=request.values.get("name")   
    image_url=request.values.get("image_url") 
    min_players=request.values.get("min_players")    
    max_players=request.values.get("max_players")    
    min_playtime=request.values.get("min_playtime")
    max_playtime=request.values.get("max_playtime")
    min_age=request.values.get("min_age")    
    id=request.values.get("_id")    
    boardgames.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "image_url":image_url, "min_players":min_players, "max_players":max_players, "min_playtime":min_playtime, "max_playtime":max_playtime, "min_age":min_age }})    
    return redirect("/list")       
    
if __name__ == "__main__":    
    
    app.run()   