from flask import Flask, render_template, request, redirect, url_for, jsonify
from helpers import extract_positions

app = Flask(__name__)

quiz1_answer = []

quiz2_answer = []

quiz3_answer = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz/1", methods=["GET", "POST"])
def quiz1_submit():
    if request.method == "GET":
        return render_template("quiz1.html")
    else:
        extract_positions(request)
        return jsonify({"redirect": "/quiz/2"})


@app.route("/quiz/2", methods=["GET", "POST"])
def quiz2_submit():
    if request.method == "GET":
        return render_template("quiz2.html")
    else:
        extract_positions(request)
        
        return jsonify({"redirect": "/quiz/3"})


@app.route("/quiz/3", methods=["GET", "POST"])
def quiz3_submit():
    if request.method == "GET":
        return render_template("quiz3.html")
    else:
        return jsonify({"redirect": "/quiz/result"})


@app.route("/quiz/result")
def quiz_result():
    return render_template("quiz_result.html", score=6)

@app.route("/lesson", methods=["GET"])
def lesson():
    return render_template("lesson.html")


if __name__ == "__main__":
    app.run(debug=True)
