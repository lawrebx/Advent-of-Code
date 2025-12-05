input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

fresh_ids = input[:input.index('')]


available_ids = input[input.index('')+1:]

fresh_ready_ids = []
fresh_ready_count = 0

for avail_id in available_ids:
    for fresh_id in fresh_ids:
        fresh_id_range_points = fresh_id.split('-')
        if int(avail_id) >= int(fresh_id_range_points[0]):
            if int(avail_id) <= int(fresh_id_range_points[1]):
                fresh_ready_ids.append(avail_id)
                fresh_ready_count = fresh_ready_count + 1
                break

#print(fresh_ready_count)

confirm_ids = []
check_ids = input[:input.index('')]

found_overlaps = 1

overlap_count = 0

def check_id(tgt_id, check_list, debug_level=0):
        
        check_list.pop(check_list.index(tgt_id))
        
        # ['1-5','3-8','10-15']
        #'1-5' <- ['3-8','10-15'] pop it out

        if debug_level >= 2:
            print(f'Checking for overlap of {tgt_id} in range {check_list}')

        overlap_flag = 0

        tgt_id_range_points = tgt_id.split('-')
        tgt_min = int(tgt_id_range_points[0])
        tgt_max = int(tgt_id_range_points[1])
        new_id = f'{tgt_min}-{tgt_max}'

        for check_id in check_list:
            
            if debug_level >= 2:
                print(f'Checking Value: {check_id}')
                print(f'Check List: {check_list}')
            check_list.pop(check_list.index(check_id))
            if debug_level >= 2:
                print(f'Check List Popped: {check_list}')

            if debug_level >= 1:
                if check_id == '95663575055329-96633400526822':
                    debug_level = 2

            check_id_range_points = check_id.split('-')

            check_min = int(check_id_range_points[0])
            check_max = int(check_id_range_points[1])

            if debug_level >= 2:
                print(f'Target Min: {tgt_min} | Target Max: {tgt_max}')
                print(f'Check Min: {check_min} | Check Max: {check_max}')

            if check_min <= tgt_min <= check_max:

                if tgt_max > check_max:
                    check_max = tgt_max

                if debug_level >= 1:
                    print(f'Popped {check_id} from final matches!')
                    print(f'min bound - {tgt_id} overlaps {check_id} - updating checklist to include [{check_min}-{check_max}]!')
                overlap_flag = 1
                new_id = f'{check_min}-{check_max}'
                break

            elif check_min <= tgt_max <= check_max:

                if tgt_min < check_min:
                    check_min = tgt_min

                if debug_level >= 1:
                    print(f'Popped {check_id} from final matches!')
                    print(f'max bound - {tgt_id} overlaps {check_id} - updating checklist to include [{check_min}-{check_max}]!')
                overlap_flag = 1
                new_id = f'{check_min}-{check_max}'
                break

            elif check_id == tgt_id:
                print(f'ID MATCH!')
                if debug_level >= 2:
                    print(f'Range {tgt_id} matches {check_id}!')
                pass
            
            else:
                check_list.insert(0,check_id)
                if debug_level >= 2:
                    print(f'{tgt_id} does not overlap {check_id} - added back to check list.')
                pass

        if overlap_flag == 0:
            new_id = f'{tgt_min}-{tgt_max}'
            if debug_level >= 1:
                print(f'{tgt_id} did not overlap any ranges!')
        else:
            if debug_level >= 1:
                print(f'{tgt_id} - adding {new_id} to check_list')

        return new_id, 0

final_ranges = []

final_flag = 0
iter_check = 0

print(len(check_ids))

final_ranges = input[:input.index('')]

while iter_check < 5:

    #if iter_check > 4:
    #    break
    
    tgt_id = final_ranges[0]

    debug = 0

    if debug >= 1:
        print(f'Iteration {iter_check} checking {tgt_id} against {len(final_ranges)} ids ////////////////////////////////////')

    new_id, final_check = check_id(tgt_id, final_ranges, debug)

    if debug >= 1:
        print(final_ranges)
        print(f'Result - add {new_id} - {len(final_ranges)} ids ////////////////////////////////////')
        final_ranges.append(new_id)
        print(final_ranges)

    iter_check = iter_check + 1

final_count = 0
total_count = 0

final_ranges = list(set(final_ranges))

print(final_ranges)

with open('output.txt', "w") as file:
    for item in final_ranges:
        file.write(item + "\n")

for final_range in final_ranges:
    range_points = final_range.split('-')
    id_count = (int(range_points[1]) - int(range_points[0]))+1
    final_count = final_count + id_count

for fresh_id in fresh_ids:
    fresh_points = fresh_id.split('-')
    id_count = (int(fresh_points[1]) - int(fresh_points[0]))+1
    total_count = total_count + id_count

print(total_count)

print(final_count)
