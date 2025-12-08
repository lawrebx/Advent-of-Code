input = []

with open('input_test.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

inputs = [line.split(' ') for line in input]

inputs_filtered = []

for line in inputs:
    inputs_filtered.append([item for item in line if item and item.strip()])

calc_dict = {}

ops_line = None

calc_input = inputs_filtered.pop()

for line in inputs_filtered:
    if calc_dict == {}:
        calc_dict = {index: [int(value)] for index, value in enumerate(line)}
    else:
        append_dict = {index: [int(value)] for index, value in enumerate(line)}

        for entry in calc_dict:
            calc_dict[entry].extend(append_dict[entry])

print(calc_dict)

final_res = 0

for cidx, calc in enumerate(calc_input):

    calc_ints = calc_dict[cidx]

    cres = None

    for cint in calc_ints:
        if cres == None:
            cres = cint
        else:
            if calc == '*':
                cres *= cint
            else:
                cres += cint
    
    print(f'Inputs: {calc_ints} | Operation: {calc} | Sum Result: {cres}')

    if cres == None:
        print('ERROR')
    else:
        final_res = final_res + cres

print(final_res)


