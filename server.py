from flask import Flask, render_template, request, redirect, url_for, jsonify
from helpers import extract_positions, get_final_score, calculate_direction_with_positions

app = Flask(__name__)

answers_data = [0]*4

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz/1", methods=["GET", "POST"])
def quiz1_submit():
    if request.method == "GET":
        return render_template("quiz1.html")
    else:
        positions = extract_positions(request)
        distance, direction = calculate_direction_with_positions(positions)
        answers_data[0] = [distance, direction]
        return jsonify({"redirect": "/quiz/2"})


@app.route("/quiz/2", methods=["GET", "POST"])
def quiz2_submit():
    if request.method == "GET":
        return render_template("quiz2.html")
    else:
        positions = extract_positions(request)
        distance, direction = calculate_direction_with_positions(positions)
        answers_data[1] = [distance, direction]
        return jsonify({"redirect": "/quiz/3"})


@app.route("/quiz/3", methods=["GET", "POST"])
def quiz3_submit():
    if request.method == "GET":
        return render_template("quiz3.html")
    else:
        positions = extract_positions(request)
        distance, direction = calculate_direction_with_positions(positions)
        answers_data[2] = [distance, direction]
        return jsonify({"redirect": "/quiz/4"})

@app.route("/quiz/4", methods=["GET", "POST"])
def quiz4_submit():
    if request.method == "GET":
        return render_template("quiz4.html")
    else:
        answer = request.json["answer"]
        answers_data[3] = answer
        return jsonify({"redirect": "/quiz/result"})


@app.route("/quiz/result")
def quiz_result():
    final_score = get_final_score(answers_data)
    print(final_score)
    return render_template("quiz_result.html", score=final_score)

@app.route("/lesson", methods=["GET"])
def lesson():
    return render_template("lesson.html")


if __name__ == "__main__":
    app.run(debug=True)
