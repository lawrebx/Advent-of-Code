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

for combo in combo_list:
    print(combo)


