import sys, os

input_file = os.path.dirname(sys.argv[0])+'/input.txt'

steps = []

with open(input_file) as f:
    for line in f:
        steps.append(line.strip().split(' '))
 
#print(steps)

monkey_attr = []
attr_list = []

for step in steps:
    if step != ['']:
        monkey_attr.append(step)
    else:
        attr_list.append(monkey_attr)
        monkey_attr = []

print(attr_list[0])