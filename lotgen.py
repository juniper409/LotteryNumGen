'''
Program: NumGen
Purpose: Generate randomized numbers.
Author: CB Juniper

This program is experimental. Please use at your own risk.

Please submit any issues or requests to mrjuniper409 [at] gmail.com

'''
# Comment for Git.
import NumGen
game_name = 'Megaball'
play = 0
play_number = int(input("How many plays? (1-5)"))

while play < play_number:
    NumGen.generate(game_name, game_name)
    play +=1
