import random

while(True):
    user_input = input('Enter command: ')
    if user_input == 'r':
        print(random.randint(1,4))
    elif user_input == 'q':
        print('quit selected')
        break
    else:
        print('invalid command')

