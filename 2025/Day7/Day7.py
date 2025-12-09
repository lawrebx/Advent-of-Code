input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

spaces = len(input[0])

previous_layer = list(input.pop(0))
split_count = 0

result = []

for layers in input:
    layer = list(layers)
    result.append(previous_layer)
    for s in range(0,spaces):
        #check space value
        if layer[s] == '^':
            #print('splitter!')
            if previous_layer[s] == 'S' or previous_layer[s] == '|':
                #print('splitting beams!')
                if s-1 >= 0:
                    layer[s-1] = '|'
                if s+1 <= spaces:
                    layer[s+1] = '|'
                split_count = split_count + 1
        else:
            if previous_layer[s] == 'S' or previous_layer[s] == '|':
                layer[s] = '|'

    previous_layer = layer

print(f'Part 1 Answer: {split_count}')

count_array = [0] * spaces

input = []
count_results = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

for line in input:
    for c in range(0,spaces): 

        path_count = count_array[c]
        if line[c] == 'S':
            count_array[c] = count_array[c] + 1
        elif line[c] == '^':
            if count_array[c] > 0:
                count_array[c] = 0
            if c - 1 >= 0:
                count_array[c-1] = count_array[c-1] + path_count
            if c + 1 <= spaces:
                count_array[c+1] = count_array[c+1] + path_count
    count_results.append(count_array.copy())

'''
for line in input:
    print(line)
for ca in count_results:
    print(ca)
'''

print(f'Part 2 Answer: {sum(count_array)}')