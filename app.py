from flask import Flask, render_template, request, jsonify
import requests as apirequest

app=Flask(__name__)

@app.route("/")
def index():
    weather=[]
    if request.args.get("search") is not None:
        search=request.args.get("search")
        response=apirequest.get(f"http://api.openweathermap.org/data/2.5/weather?q={search}&appid=___###API_KEY_HERE###___")
        data=response.json()
        weather=data["main"]
    return render_template("index.html", weather=weather)
