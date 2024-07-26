# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.

patterns = {}

def player(prev_play, opponent_history=[]):
    if prev_play != '':
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    guess = 'R'

    n = 3
    if len(opponent_history) > n:
        current_pattern = ''.join(opponent_history[-n:])

        if ''.join(opponent_history[-(n + 1):]) in patterns.keys():
            patterns[''.join(opponent_history[-(n + 1):])] += 1
        else:
            patterns[''.join(opponent_history[-(n + 1):])] = 1

        possible_patterns = [current_pattern + 'R', current_pattern + 'P', current_pattern + 'S']

        for i in possible_patterns:
            if not i in patterns.keys():
                patterns[i] = 0

        next_move = max(possible_patterns, key=lambda key: patterns[key])

        if next_move[-1] == 'R':
            guess = 'P'
        elif next_move[-1] == 'P':
            guess = 'S'
        elif next_move[-1] == 'S':
            guess = 'R'

    return guess
