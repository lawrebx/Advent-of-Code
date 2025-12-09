input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        cleaned = line.replace("\n", ' ')
        input.append(cleaned)

inputs = [line for line in input]

inputs_filtered = []

for line in inputs:
    inputs_filtered.append([item for item in line if item and item.strip()])

calc_input = inputs_filtered.pop()

inputs.pop()

cols = 0

for line in inputs:
    if len(line) > cols:
        cols = len(line)

rows = len(inputs)

digit_length = 4

calc_dict = {}
calc_list = []
val_list = []

calc_count = 0

#print(inputs)

for c in range(0,cols):

    vals = []

    for r in range(0,rows):
        new_val = inputs[r][c]
        if new_val == ' ':
            pass
        else:
            vals.append(new_val)
    
    vals = ''.join(vals)

    #print(vals)

    if vals == '' or '':
        val_list = [int(item) for item in val_list]
        calc_list.append(val_list)
        val_list = []
    else:
        val_list.append(vals)

    #print(calc_list)

final_res = 0

for cidx, calc in enumerate(calc_input):

    calc_ints = calc_list[cidx]

    cres = None

    for cint in calc_ints:
        if cres == None:
            cres = cint
        else:
            if calc == '*':
                cres *= cint
            else:
                cres += cint
    
    #print(f'Inputs: {calc_ints} | Operation: {calc} | Sum Result: {cres}')

    if cres == None:
        print('ERROR')
    else:
        final_res = final_res + cres

print(final_res)

