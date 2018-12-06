import random

def play(streak_target, num_options):

    round_counter = 0
    win_counter = 0
    print(f'streak_target: {streak_target}')
    print(f'num_options: {num_options}')

    while(True):
        user_input = input(f'Pick a number between 1 and {num_options} or choose a command: ')
        target = random.randint(1,int(num_options))

        if int(user_input) == target:
            win_counter += 1
            round_counter += 1

            if win_counter == int(streak_target):
                print(f"Congrats you're 1 in a million! You managed a streak of {win_counter} in {round_counter} rounds")
                break
                return
            print(f'Correct! Streak: {win_counter}, Rounds: {round_counter}')
        elif int(user_input) != target:
            win_counter = 0
            round_counter += 1
            print(f'Wrong! Start Over!  Streak: {win_counter}, Rounds: {round_counter}')

        elif user_input == 'q':
            print('quit selected')
            break
            return
        else:
            print('invalid command')


game_params = input('streak target, num of choices: ')

if ',' in game_params:
    game_params = game_params.split(',')
    play(int(game_params[0]), int(game_params[1]))
else:
    game_params = game_params.split()
    play(int(game_params[0]), int(game_params[1]))

# if round_counter == 1000000: print(You're very unluck, keep going)
