input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

input_ids = [tuple(map(int,s.split('-'))) for s in input[:input.index('')]]
fresh_ids = [tuple(map(int,s.split('-'))) for s in input[:input.index('')]]

srt = 1

if srt == 1:
    input_ids = sorted(input_ids)
    fresh_ids = sorted(fresh_ids)


with open('sorted_input.txt', "w") as file:
    for item in fresh_ids:
        file.write(str(item) + "\n")

similar_ranges = 0

overlap_count = 1

validated_ids = []

for id in input_ids:

    tgt_min = int(id[0])
    tgt_max = int(id[1])

    if tgt_min ==  4032864012375:
        debug = 1
    else:
        debug = 0

    if debug == 1:
        print(f'--------------- CHECKING RANGE {id} -----------------------------')

    for vr_index, vr in enumerate(fresh_ids):

        if tgt_min ==  4032864012375:
            print(f'CHECKING INDEX {vr_index} - VALUE {vr}')
            debug = 1
        else:
            debug = 0


        del_id = None

        if debug == 1:
            print(f'--------------- CHECKING RANGE {id} AGAINST INDEX {vr_index} - VALUE {vr} -----------------------------')

        check_min = int(vr[0])
        check_max = int(vr[1])
        overlap_flag = 1

        if tgt_min == check_min and tgt_max == check_max:
            del_id = fresh_ids.pop(vr_index)
            if debug == 1:
                print(f'tgt id matches check id {check_min}-{check_max} - popped {del_id}')
        elif check_min <= tgt_min <= check_max:
            del_id = fresh_ids.pop(vr_index)
            if debug == 1:
                print(f'------ Overlap ------ tgt min falls within check range {check_min}-{check_max} - popped {del_id}')
            tgt_min = check_min
            if check_min <= tgt_max <= check_max:
                tgt_max = check_max
                if debug == 1:
                    print(f'------ Double Overlap ------ tgt max falls within check range {check_min}-{check_max} - popped {del_id}')
        elif check_min <= tgt_max <= check_max:
            del_id = fresh_ids.pop(vr_index)
            if debug == 1:
                print(f'------ Overlap ------ tgt max falls within check range {check_min}-{check_max} - popped {del_id}')
            tgt_max = check_max
        elif tgt_min < check_min and tgt_max > check_max:
             del_id = fresh_ids.pop(vr_index)
             if debug == 1:
                print(f'------ Overlap ------ tgt range is superset of check range {check_min}-{check_max} - popped {del_id}')
        else:
            if debug == 1:
                print(f'------ No Overlap ------ tgt range no in check range {check_min}-{check_max}')
            overlap_flag = 0
        
        if debug == 1:
            if overlap_flag == 1:
                print(f'!!!!! new tgt id = {(tgt_min,tgt_max)}')
            else:
                print(f'////// no overlap - target range remains {(tgt_min,tgt_max)}')

    if debug == 1:
        print(f'ADDING {(tgt_min,tgt_max)} to fresh_ids')

    validated_ids.append((tgt_min,tgt_max))

    fresh_ids.append((tgt_min,tgt_max))


#print(valid_ranges)

final_count = 0

for final_range in fresh_ids:
    id_count = (int(final_range[1]) - int(final_range[0]))+1
    final_count = final_count + id_count

with open('sorted_output.txt', "w") as file:
    for item in sorted(fresh_ids):
        file.write(str(f'{item[0]}-{item[1]}') + "\n")

with open('validated_ids.txt', "w") as file:
    for item in validated_ids:
        file.write(str(f'{item[0]}-{item[1]}') + "\n")

print(final_count)