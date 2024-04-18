CORRECT_ANSWERS = ["c"]*5

def extract_positions(request):
    # format is in 
    # {'position_1': {'left': 45, 'top': 0}, 
    # 'position_2': {'left': 700.99609375, 'top': 90}, 
    # 'position_3': {'left': 45, 'top': 250}, 
    # 'position_4': {'left': 45, 'top': 375}, 
    # 'position_5': {'left': 45, 'top': 500}}
    print(request.json)
    return request.json


def calculate_direction_with_positions(positions):
    # calculate the absolute distance and direction to the pg
    distance, direction = positions["position_1"], positions["position_2"]
    return distance, direction


def get_final_score(answers):
    final_score = 0
    for i, answer in enumerate(answers):
        if answer == CORRECT_ANSWERS[i]:
            final_score += 2.5

    return final_score