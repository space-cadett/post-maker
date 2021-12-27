from flask import Flask,render_template
from bs4 import BeautifulSoup
import flask
import requests

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    outerdata = soup.find_all("div",class_= "widget-listing" ,limit=5)
    finalNews=""
    for data in outerdata:
        news = data.div.a["title"]
        finalNews += "\u2022 " + news + "\n"
    return render_template("index.html", News=finalNews)
