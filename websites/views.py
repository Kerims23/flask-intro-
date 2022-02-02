from flask import Blueprint, render_template 

views = Blueprint("views", __name__)

@views.route("/")
def home():
  name = "kerim"
  return render_template("index.html", name = name)