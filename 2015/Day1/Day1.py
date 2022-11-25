import sys, os
             
input_file = os.path.dirname(sys.argv[0])+'/input.txt'
inputs = [char for char in open(input_file).read()]

################################ PART ONE ################################
"""
An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

"""

input_map = {
                    ')':-1,
                    '(':1
                   }

def instruction_decoder(input_list=list,instruction_dict=dict):
    
    output_list =  [instruction_dict[input] for input in input_list]

    return output_list

instructions = instruction_decoder(inputs,input_map)

final_floor = sum(instructions)

print(f'To what floor do the instructions take Santa?\nAnswer: Floor {final_floor}')

################################ PART TWO ################################
"""
--- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?

"""

current_floor = 0
current_step = 0

for step in instructions:
    current_step = current_step + 1
    current_floor = current_floor + step

    if current_floor == -1:
        print(f'What is the position of the character that causes Santa to first enter the basement?\nAnswer: Step {current_step}')
        break