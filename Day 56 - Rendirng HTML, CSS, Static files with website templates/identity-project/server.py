from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# __name__ is the special attribute in python

if __name__ == "__main__":
    app.run(debug=True)