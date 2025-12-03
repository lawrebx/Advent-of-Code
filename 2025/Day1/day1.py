input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

dial_pos = 50
tgt_pos = 0
combination = 0
combination_p2 = 0

for move in input:

    zero_pos = False
    hit_zero = False
    clicks = 0

    start_pos = dial_pos

    direction = move[:1]
    magnitude = int(move[1:])
    if magnitude > 100:
        clicks = magnitude // 100
        magnitude = magnitude%100
        
    if direction == 'L':
        magnitude = magnitude * -1
    
    dial_pos = dial_pos + magnitude

    if dial_pos < 0:
        dial_pos = 100 + dial_pos
        hit_zero = True
    elif dial_pos > 99:
        dial_pos = dial_pos - 100
        hit_zero = True
    elif dial_pos == tgt_pos:
        hit_zero = True

    if start_pos != 0 and hit_zero == True:
        clicks = clicks + 1
        

    if dial_pos == tgt_pos:
        combination = combination + 1
        zero_pos = True

    combination_p2 = combination_p2 + clicks

    #print(f'Move: {move} | direction {direction} | magnitude {magnitude} | Dial Start {start_pos} | Dial End {dial_pos} | Clicks {clicks} | At Zero {zero_pos}')

print(f'Combination Part 1: {combination}')
print(f'Combination Part 2: {combination_p2}')