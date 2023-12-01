import sys, os
             
input_file = os.path.dirname(sys.argv[0])+'/input.txt'
with open(input_file) as f:
    calibration_input = [line.rstrip() for line in f]

################################ PART ONE ################################
"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, 
they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked 
when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") 
and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") 
when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently 
just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
"""
line_count = 0
calibration_values = []

for line in calibration_input:
    line_count = line_count + 1
    line_digits = [int(s) for s in list(line) if s.isdigit()]
    if len(line_digits) == 0:
        raise Exception(f'Line read error - no coordinates found in line {line_count}.')
    elif len(line_digits) > 0:
        _calibration_value = int(str(line_digits[0]) + str(line_digits[-1]))
        calibration_values.append(_calibration_value)
    else:
        raise Exception(f'Line read error - Unable to parse line {line_count}.')
    
print(f'Part 1 - The sum of the calibration values is {sum(calibration_values)}')

"""

################################ PART TWO ################################
"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

"""
number_dict = {'one':'1', 
                'two':'2', 
                'three':'3', 
                'four':'4', 
                'five':'5', 
                'six':'6', 
                'seven':'7', 
                'eight':'8', 
                'nine':'9'}

line_count = 0
calibration_values = []

#calibration_input = calibration_input[0:9]

for line in calibration_input:
    raw_line = line
    # break down into array to track integer positions
    line_int = list(line)
    line_digits = []
    for i, v in enumerate(line_int):
        if v.isdigit():
            line_digits.append(v) 
        else:
            for key, val in number_dict.items():
                if ''.join(line_int[i:]).find(key) == 0:
                    line_digits.append(number_dict[key]) 
                else:
                    pass

    if len(line_digits) == 0:
        raise Exception(f'Line read error - no coordinates found in line {line_count}.')
    elif len(line_digits) > 0:
        _calibration_value = int(str(line_digits[0]) + str(line_digits[-1]))
        calibration_values.append(_calibration_value)
    else:
        raise Exception(f'Line read error - Unable to parse line {line_count}.')

    print(f'Raw Line:{raw_line}')
    print(f'Extracted Digits:{line_digits}')
    print(f'Calibration Values: {_calibration_value}')
    
print(f'Part 2 - The sum of the calibration values is {sum(calibration_values)}')
