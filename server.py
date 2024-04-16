from flask import Flask, render_template


app = Flask(__name__)

quiz1_answer = []

quiz2_answer = []

quiz3_answer = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz/1")
def quiz1_submit():
    return render_template("quiz.html")


@app.route("/quiz/2")
def quiz2_submit():
    return render_template("index.html")


@app.route("/quiz/3")
def quiz3_submit():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
