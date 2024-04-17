def extract_positions(request):
    # format is in 
    # {'position_1': {'left': 45, 'top': 0}, 
    # 'position_2': {'left': 700.99609375, 'top': 90}, 
    # 'position_3': {'left': 45, 'top': 250}, 
    # 'position_4': {'left': 45, 'top': 375}, 
    # 'position_5': {'left': 45, 'top': 500}}
    print(request.json)
