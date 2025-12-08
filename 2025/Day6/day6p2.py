input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line)

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

digit_length = 3

calc_dict = {}
calc_list = []

calc_count = 0

for r in range(0,rows):

    calc_dict = {}

    calc_row = inputs[r]

    #print(f'Cal Row: {calc_row}')

    for c in range(0,cols):
        #print(f'Calc Row: {calc_row[c]}')
        calc_dict[c] = calc_row[c]

    calc_list.append(calc_dict)

#print(calc_list)

calc_dict_final = {}

for calc_row in calc_list:
    for c in range(0,cols):
        try:
            calc_dict_final[c] = str(calc_dict_final[c]) + str(calc_row[c])
        except:
            calc_dict_final[c] = str(calc_row[c])

#print(calc_dict_final)

new_digit = ''

digit_list = []
calcs = []

for i in range(0,rows):   

    if (i+1) % (digit_length+1) == 0:
        #print(f'{i} - NEXT CALCULATION!!!')
        calcs.append(digit_list)
        digit_list = []
    else: 
        try:
            new_digits = "".join(calc_dict_final[i].replace('\n', '').replace('\r', '').split())
            digit_list.append(int(new_digits))
        except Exception as e:
            print(i)
            print(calc_dict_final)
            print(calc_dict_final[i])
            print(e)
            break

#print(calcs)

final_res = 0

print(len(calc_input))

for cidx, calc in enumerate(calc_input):

    calc_ints = calcs[cidx]

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