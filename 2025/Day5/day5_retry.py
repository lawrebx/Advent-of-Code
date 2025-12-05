input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

fresh_ids = [tuple(map(int,s.split('-'))) for s in input[:input.index('')]]

valid_ranges = []

similar_ranges = 0

overlap_count = 1

while overlap_count > 0:

    print('RESETTING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    if valid_ranges != []:
        fresh_ids = valid_ranges

    overlap_count = 0 

    for id in fresh_ids:

        print(f'--------------- CHECKING RANGE {id} -----------------------------')

        overlap_flag = 0

        for vr_index, vr in enumerate(valid_ranges):

            check_min = vr[0]
            check_max = vr[1]

            tgt_min = id[0]
            tgt_max = id[1]

            if id == vr:
                print('tgt matches check id')
                overlap_flag = 0
                break

            elif check_min <= tgt_min <= check_max:
                overlap_flag = 1
                print('tgt min within check range, maintaining check_min')
                if check_min <= tgt_max <= check_max:
                    print('tgt range within check range - exiting')
                else:
                    print('tgt max larger than check max, extending and updating range')
                    check_max = tgt_max
                
                print('Range max extended - moving to next id')
                valid_ranges[vr_index] = (check_min,check_max)
                break
            elif check_min <= tgt_min <= check_max:
                overlap_flag = 1
                print('tgt max within check range, maintaining check_max')
                if check_min <= tgt_min <= check_max:
                    print('tgt range within check range - exiting')
                else:
                    print('tgt min smaller than check min, extending and updating range')
                    check_min = tgt_min

                print('Range min extended - moving to next id')
                valid_ranges[vr_index] = (check_min,check_max)
                break
            
            else:
                overlap_flag = 0
                
        
        if overlap_flag == 0:
            print(f'No overlap! Appending {id} to ranges')
            valid_ranges.append(id)
        else:
            overlap_count = overlap_count + overlap_flag

#print(valid_ranges)

final_count = 0

for final_range in valid_ranges:
    id_count = (int(final_range[1]) - int(final_range[0]))+1
    final_count = final_count + id_count

print(final_count)