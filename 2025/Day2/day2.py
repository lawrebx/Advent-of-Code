with open('input.txt', 'r') as f:
    # Read the entire content of the file
    content = f.read()

id_list = content.split(',')

id_sum = 0
id_sum2 = 0

def id_check(id_int):

    id = str(id_int)

    valid = True
    valid2 = True

    # get len of string, split in half, work back to 1
    id_length = len(id)
    pattern_length = id_length//2

    #print(f'CHECK {id}: {id[:pattern_length]} | {id[pattern_length:]}')

    if id[:pattern_length] == id[pattern_length:]:
        #print("invalid id!")
        valid = False
        return valid, valid2
    else:
        #print('checking sequences!')
        pattern_length = pattern_length - 1
        if pattern_length == 0:
            pattern_length = 1
        while pattern_length > 0 and valid == True:
            #print(f'Pattern Length: {pattern_length} | {pattern_length} | {id_length} | {id_length % pattern_length}')
            if id_length % pattern_length == 0:
                unit_count = id_length // pattern_length
                units = []
                i = 0
                for n in range(0,unit_count):
                    units.append(id[n*pattern_length:(n*pattern_length)+(pattern_length)])

                #print(units)

                if len(set(units)) == 1 and len(units) > 1:
                    valid2 = False
                    return valid, valid2
                
            pattern_length = pattern_length - 1

    return valid, valid2

#id_list = ['11-22']

for id_range in id_list:
    #print(id_range)
    id_split = id_range.split('-')
    for id in range(int(id_split[0]),int(id_split[1])+1):
        
        check1, check2 = id_check(id)
        if check1 == False:
            id_sum = id_sum + int(id)
            id_sum2 = id_sum2 + int(id)
        elif check2 == False:
            id_sum2 = id_sum2 + int(id)
        #if check1 == False or check2 == False:    
            #print(f'{id} | {check1} | {check2}')

print(f'Part 1 Sum: {id_sum}')
print(f'Part 2 Sum: {id_sum2}')
    