from http.client import responses
from flask import Flask, render_template
import random
import datetime as dt
import requests


age_endpoint = "https://api.agify.io"
gender_endpoint = "https://api.genderize.io"

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = dt.datetime.now().year
    return render_template(
        "index.html",
        num=random_number,
        year=current_year
        )

# Calling with API
@app.route("/guess/<guess_name>")
def guess_age_gen(guess_name):
    param = {
        "name" : guess_name
    }
    age_response = requests.get(age_endpoint,params=param)
    gender_response = requests.get(gender_endpoint,params=param)
    age = age_response.json()['age']
    gender = gender_response.json()['gender']
    return render_template(
        "guess.html",
        name=guess_name,
        gender=gender,
        age = age
    )

# Looping and Condition with Jinjer template
@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts=all_posts)

# __name__ is the special attribute in python

if __name__ == "__main__":
    app.run(debug=True)