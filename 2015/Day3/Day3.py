import sys, os
             
input_file = os.path.dirname(sys.argv[0])+'/input.txt'

move_list = [char for char in open(input_file).read()]

################################ PART ONE ################################
"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, 
and then an elf at the North Pole calls him via radio and tells him where to move next. 
Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
After each move, he delivers another present to the house at his new location.

Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""

move_map = {
                '^':[0,1],
                'v':[0,-1],
                '>':[1,0],
                '<':[-1,0]
                }

def get_visited_houses(input_list=list, starting_position=list, input_map=dict):
    
    current_position = starting_position
    homes_visited = [''.join(str(starting_position))]
    
    for move in input_list:
        current_move = input_map[move]
        current_position = [sum(x) for x in zip(current_move, current_position)]
        homes_visited.append(''.join(str(current_position)))

    return homes_visited

unique_visits = len(set(get_visited_houses(move_list,[0,0],move_map)))

if unique_visits > 1:
    plural = 's'
else:
    plural = ''

print(f'How many houses receive at least one present?\nAnswer: {unique_visits} house{plural}.')

################################ PART TWO ################################
"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

santa_list = move_list[::2]
robo_santa_list = move_list[1::2]

santa_visits = get_visited_houses(santa_list,[0,0],move_map)
robo_santa_visits = get_visited_houses(robo_santa_list,[0,0],move_map)

unique_visit_list = set(santa_visits + robo_santa_visits)

unique_visits = len(set(unique_visit_list))
unique_santa_visits = len(set(santa_visits))
unique_robo_santa_visits = len(robo_santa_visits)

if unique_visits == 1:
    plural = ''
else:
    plural = '0'

print(f'This year, how many houses receive at least one present?\nAnswer: {unique_visits} house{plural}.')

if unique_santa_visits == 1:
    plural = ''
else:
    plural = 's'

print(f'This year, how many houses receive at least one present from Santa?\nAnswer: {unique_santa_visits } house{plural}.')

if unique_robo_santa_visits == 1:
    plural = ''
else:
    plural = 's'

print(f'This year, how many houses receive at least one present from Robo-Santa?\nAnswer: {unique_robo_santa_visits} house{plural}.')