CORRECT_ANSWER = [
    [(403, 179), (567, 254), (384, 437), (552, 471), (703, 462)],
    [(443, 191), (603, 233), (358, 423), (499, 428), (695, 425)],
    [(554, 121), (666, 239), (438, 441), (612, 378), (777, 456)],
    "c",
]

THRETHOLD = 1000


def extract_positions(request):
    # format is in
    # {'position_1': {'left': 45, 'top': 0},
    # 'position_2': {'left': 700.99609375, 'top': 90},
    # 'position_3': {'left': 45, 'top': 250},
    # 'position_4': {'left': 45, 'top': 375},
    # 'position_5': {'left': 45, 'top': 500}}

    return [
        (request.json[pos]["left"], request.json[pos]["top"]) for pos in request.json
    ]


def check_answer(my_answer, correct):
    result = 0
    for i in range(len(my_answer)):
        dist = (my_answer[i][0] - correct[i][0]) ** 2 + (
            my_answer[i][1] - correct[i][1]
        ) ** 2
        if dist <= THRETHOLD:
            result += 0.5
    return result

def get_final_score(answers):
    final_score = 0
    for i, answer in enumerate(answers):
        if isinstance(answer, list):
            final_score += check_answer(answer, CORRECT_ANSWER[i])
        else:
            if answer == CORRECT_ANSWER[i]:
                final_score += 2.5

    return final_score
