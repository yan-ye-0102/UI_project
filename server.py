from flask import Flask, render_template, request, jsonify
from helpers import extract_positions, get_final_score

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
        answers_data[0] = positions
        return jsonify({"redirect": "/quiz/1/result"})

@app.route("/quiz/1/result", methods=["GET"])
def quiz1_result():
    return render_template("quiz1_result.html")

@app.route("/quiz/2", methods=["GET", "POST"])
def quiz2_submit():
    if request.method == "GET":
        return render_template("quiz2.html")
    else:
        positions = extract_positions(request)
        answers_data[1] = positions
        return jsonify({"redirect": "/quiz/2/result"})

@app.route("/quiz/2/result", methods=["GET"])
def quiz2_result():
    return render_template("quiz2_result.html")

@app.route("/quiz/3", methods=["GET", "POST"])
def quiz3_submit():
    if request.method == "GET":
        return render_template("quiz3.html")
    else:
        positions = extract_positions(request)
        answers_data[2] = positions
        return jsonify({"redirect": "/quiz/3/result"})

@app.route("/quiz/3/result", methods=["GET"])
def quiz3_result():
    return render_template("quiz3_result.html")

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
    print(answers_data)
    return render_template("quiz_result.html", score=final_score)

@app.route("/lesson", methods=["GET"])
def lesson():
    return render_template("lesson.html")



@app.route("/combined-setup")
def combined_setup():
    return render_template("combined_setup.html")

if __name__ == "__main__":
    app.run(debug=True)
