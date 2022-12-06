import sys, os
             
input_file = os.path.dirname(sys.argv[0])+'/input.txt'
with open(input_file) as f:
    input = [line.rstrip('\n') for line in f]

################################ PART ONE ################################
"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
entry_size = 4

for i, line in enumerate(input):
    if line == '':
        start_proc = i
        break

stackline = input[i-1]
stacks = [int(stackline[i:i+entry_size].strip()) for i in range(0, len(stackline), entry_size)]

arrangement = []

for line in range(0,start_proc-1,1):
    testline = input[line]
    arrangement.append([testline[i:i+entry_size].rstrip() for i in range(0, len(testline), entry_size)])

arrangement.reverse()

stacked_boxes = []

for i, stack in enumerate(stacks):
    stack_list=[]
    for line in arrangement:
        stack_list.append(line[i])
    stack_list = [i for i in stack_list if i]
    stacked_boxes.append(stack_list)

procedures = []
for line in range(start_proc+1,len(input),1):
    proc_step = input[line].split(' ')
    procedures.append([int(proc_step[1]),int(proc_step[3]),int(proc_step[5])])

for step in procedures:
    box_count = step[0]
    from_stack = step[1]
    to_stack = step[2]

    for box in range(0,box_count,1):
        stacked_boxes[to_stack-1].append(stacked_boxes[from_stack-1].pop())

top_boxes = []

for stack in stacked_boxes:
    top_boxes.append(stack[len(stack)-1])


code = ''.join(top_boxes).replace("[",'').replace("]",'')

print(f'The final message is: {code}.')

"""

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, 
and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved 
crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves 
know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

"""

stacked_boxes = []

for i, stack in enumerate(stacks):
    stack_list=[]
    for line in arrangement:
        stack_list.append(line[i])
    stack_list = [i for i in stack_list if i]
    stacked_boxes.append(stack_list)


for step in procedures:
    box_count = step[0]
    from_stack = step[1]
    to_stack = step[2]
    move_stack = []

    for box in range(0,box_count,1):
        move_stack.append(stacked_boxes[from_stack-1].pop())
    move_stack.reverse()
    stacked_boxes[to_stack-1].extend(move_stack)

top_boxes = []

for stack in stacked_boxes:
    top_boxes.append(stack[len(stack)-1])


code = ''.join(top_boxes).replace("[",'').replace("]",'')

print(f'The final message is: {code}.')