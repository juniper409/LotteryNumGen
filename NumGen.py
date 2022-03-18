
'''
Program: NumGen
Purpose: Generate randomized numbers.
Author: CB Juniper

This program is experimental. Please use at your own risk.

Please submit any issues or requests to mrjuniper409 [at] gmail.com

'''
import random



def generate(game_name, ball_name):
    lottery_numbers = []
    extra_ball = []
    for i in range (0,5):
        number = random.randint(1,41)
        lottery_numbers.append(number)
    for i in range (0,1):
        ball = random.randint(1,6)
        extra_ball.append(ball)



    lottery_numbers.sort()
    lottery_numbers = (str(lottery_numbers)[1:-1])
    extra_ball = (str(extra_ball)[1:-1])

    print('')
    print('>>> Your', game_name, 'Numbers: ')
    print(lottery_numbers)
    print(ball_name,'Number:',extra_ball)
    print('')
    print("GOOD LUCK!")

