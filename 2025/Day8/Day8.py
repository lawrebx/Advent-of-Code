input = []

with open('input_test.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        sline = line.strip().split(",")
        sline = [int(i) for i in sline]
        input.append(sline)

def calc_distance(input1:list,input2:list):

    distance = ((input1[0]-input2[0])**2 + (input1[1]-input2[1])**2 + (input1[2]-input2[2])**2)**0.5

    return distance

min_coords = (0,0)
combo_list = []

min_dist = None


for coord in input:
    min_dist = None
    for check_coord in input:
        if coord != check_coord:
            dist = calc_distance(coord, check_coord)
            if min_dist == None:
                min_dist = dist
                min_coords = (coord, check_coord, dist)
            elif min_dist > dist:
                min_dist = dist
                min_coords = (coord, check_coord, dist)   

    combo_list.append(min_coords)

if min_dist != None:
    print(f'Min Distance: {min_dist//1} | Min Coords {min_coords}')

print('-------------------------')
sorted_list = sorted(combo_list, key=lambda combo_list: combo_list[2])

circuits = {}
circuit_count = 0

for combo_d in sorted_list:
    combo = combo_d[0], combo_d[1]

    combo = list(combo)

    if circuits == {}:
        circuits[circuit_count] = combo
        print(circuits)
        continue

    existing_circuit = 0

    for key in circuits:
        if combo[0] in circuits[key]:
            circuits[key].extend(combo)
            continue
        elif combo[1] in circuits[key]:
            circuits[key].extend(combo)
            continue   

    circuit_count = circuit_count + 1
    circuits[circuit_count] = combo
    
    print(circuits)

sorted_circuits = dict(sorted(circuits.items(), key=lambda item: len(item[1]), reverse=True))

for c in sorted_circuits:
    print(len(circuits[c]))


