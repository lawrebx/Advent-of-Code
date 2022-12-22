import sys, os

input_file = os.path.dirname(sys.argv[0])+'/input.txt'

steps = []

with open(input_file) as f:
    for line in f:
        steps.append(line.strip().split(' '))
 
# How many elements each
# list should have
n = 40
 
# using list comprehension
rows = [steps[i * n:(i + 1) * n] for i in range((len(steps) + n - 1) // n )]
print(rows)

   print(''.join(cycle_obs),end='\n')