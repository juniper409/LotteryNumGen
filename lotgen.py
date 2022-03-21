'''
Program: NumGen
Purpose: Generate randomized numbers.
Author: CB Juniper

This program is experimental. Please use at your own risk.

Please submit any issues or requests to mrjuniper409 [at] gmail.com

'''
from NumGen import generate
game_name = 'Megabucks'
ball_name = 'Megaball'
play = 0
    
#Ask user how much plays they wish to generate.
play_number = int(input("How many plays? (1-5)"))


#While loop that will loop and return the requested amount of plays.
while play < play_number:
    print(">>> PLAY ",play,"<<<")
    generate(game_name, ball_name)
    play +=1
