from flask import (
    Flask,
    render_template
)
import requests

URL = "http://127.0.0.1:5000/users"

app = Flask(__name__)

@app.get("/")
def get_index():
    return render_template("index.html")

@app.get("/users")
def display_users():
    user_list = requests.get(URL).json()
    return render_template(
        "users.html", users = user_list.get("users")
    )

@app.get("/users/<int:pk>")
def display_user_profile(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.get(url)
    user_json = response.json().get("user")[0]
    return render_template("user.html", user=user_json)
