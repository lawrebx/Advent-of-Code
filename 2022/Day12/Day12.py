import sys, os

input_file = os.path.dirname(sys.argv[0])+'/input.txt'

################################ PART ONE ################################
"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above 
broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest 
elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly 
one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can 
be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to 
elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the 
elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, 
but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). 
The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""
grid = []

with open(input_file) as f:
    for line in f:
      row = []
      for char in line.strip():
          row.append(char)
      grid.append(row)

for row in grid:
  try: 
    print(f'Starting location: Row {grid.index(row)}, Index {row.index("S")}')
    row_pos = grid.index(row)
    col_pos = row.index("S")
  except ValueError:
    pass

for row in grid:
  try: 
    print(f'Target location: Row {grid.index(row)}, Index {row.index("E")}')
    row_tgt = grid.index(row)
    col_tgt = row.index("S")
  except ValueError:
    pass

def valid_moves(row_pos, col_pos):
  if row_pos == 0:
    up = None
  else:
    up = [row_pos - 1, col_pos]
  
  if row_pos == len(grid):
    down = None
  else:
    down = [row_pos + 1, col_pos]



