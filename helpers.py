CORRECT_ANSWERS = ["c"] * 5

CORRECT_ANSWER = [
    [(390, 190), (373, 434), (566, 257), (552, 474), (693, 461)],
    [(442, 216), (608, 239), (351, 433), (503, 427), (697, 422)],
    [(569, 115), (662, 235), (451, 450), (613, 382), (777, 456)],
    "c",
]

THRETHOLD = 5


def extract_positions(request):
    # format is in
    # {'position_1': {'left': 45, 'top': 0},
    # 'position_2': {'left': 700.99609375, 'top': 90},
    # 'position_3': {'left': 45, 'top': 250},
    # 'position_4': {'left': 45, 'top': 375},
    # 'position_5': {'left': 45, 'top': 500}}
    print(
        [(request.json[pos]["left"], request.json[pos]["top"]) for pos in request.json]
    )
    return [
        (request.json[pos]["left"], request.json[pos]["top"]) for pos in request.json
    ]


def check_answer(my_answer, correct):
    # calculate the absolute distance and direction to the pg
    for i in range(len(my_answer)):
        dist = (my_answer[i][0] - correct[i][0]) ** 2 + (
            my_answer[i][1] - correct[i][1]
        ) ** 2
        if dist > THRETHOLD:
            return False
    return True


def get_final_score(answers):
    final_score = 0
    for i, answer in enumerate(answers):
        if isinstance(answer, list):
            if check_answer(answer, CORRECT_ANSWER[i]):
                final_score += 2.5
        else:
            if answer == CORRECT_ANSWER[i]:
                final_score += 2.5

    return final_score
