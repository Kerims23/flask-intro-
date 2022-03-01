from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
  if request.method=="POST":
    name = request.form.get("name")
    age = request.form.get("age")
    return render_template("index.html", name=name, age=int(age))
  return render_template("index.html")




"""
ask the user to enter their age
if the user is older than 16 tell them they can drive
otherwise, tell them how many years until they can drive
"""