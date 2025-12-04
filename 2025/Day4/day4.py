input = []

with open('input.txt', "r", encoding="utf-8") as file:
    for count, line in enumerate(file, start=1):
        input.append(line.strip())

roll_grid = [list(item) for item in input]
roll_grid_final = [list(item) for item in input]

#roll_grid = roll_grid[:3]
#roll_grid_final = roll_grid_final[:3]

column_count = len(roll_grid[0])
row_count = len(roll_grid)

results = {}
accessible_roll_count = 0

def eval_roll(roll_pos:tuple, grid_data:list, row_range=1, col_range=1, neighbor_check = 4, col_max_index=9, row_max_index=9):

    min_col = roll_pos[0] - col_range
    max_col = roll_pos[0] + col_range

    min_row = roll_pos[1] - row_range
    max_row = roll_pos[1] + row_range

    if min_row < 0:
        min_row = min_row + 1
    
    if max_row > row_max_index:
        max_row = max_row - 1

    if min_col < 0:
        min_col = min_col + 1

    if max_col > col_max_index:
        max_col = max_col - 1

    adjacent_rolls = 0

    for c in range(min_col,max_col+1):
        for r in range(min_row,max_row+1):
            if (c,r) != roll_pos:
                if grid_data[r][c] == '@':
                    adjacent_rolls = adjacent_rolls + 1

    if adjacent_rolls >= neighbor_check:
        accessible = False
    else:
        accessible = True

    return accessible, adjacent_rolls

new_removals = 1
total_removals = 0

while new_removals > 0:
    new_removals = 0
    print(new_removals)
    for c in range(0,column_count):
        for r in range(0, row_count):
            pos = (c,r)
            if roll_grid_final[r][c] == '@':
                roll_result, adjacent_rolls = eval_roll(roll_pos = pos, grid_data = roll_grid_final, row_range=1, col_range=1, neighbor_check = 4, col_max_index=column_count-1, row_max_index=row_count-1)
                results[pos] = roll_result
                #print(f'Roll Position: {pos} | Value: {roll_grid[r][c]} | Adjacent Roll Count {adjacent_rolls} | Accessible? {roll_result}')
                if roll_result == True:
                    accessible_roll_count = accessible_roll_count + 1
                    roll_grid_final[r][c] = 'X'
                    new_removals = new_removals + 1
                    total_removals = total_removals + 1
            else:
                #print(f'Roll Position: {pos} | Value: {roll_grid[r][c]} | NOT A ROLL!')
                pass
    print(new_removals)

#print(results)
print(f'Accessible Roll Count: {accessible_roll_count}')
print(f'Total Rolls Removed: {total_removals}')

