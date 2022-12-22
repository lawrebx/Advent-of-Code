import sys, os

input_file = os.path.dirname(sys.argv[0])+'/input.txt'

################################ PART ONE ################################
"""
--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""
with open(input_file, "r") as file:
    data = file.read().splitlines()
    length = len(data)
    width = len(data[0])
    vert_data = [[x[e] for x in data] for e in range(width)]
    p1 = 0
    p2 = 0
    for y in range(length):
        for x in range(width):
            current = int(data[y][x])
            if not all((
                        any(int(z) >= current for z in data[y][:x]),
                        any(int(z) >= current for z in data[y][x + 1:]),
                        any(int(z) >= current for z in vert_data[x][:y]),
                        any(int(z) >= current for z in vert_data[x][y + 1:])
            )):
                p1 += 1
            dirs = []
            for func in (lambda y, x: (y - 1, x), lambda y, x: (y + 1, x), lambda y, x: (y, x - 1), lambda y, x: (y, x + 1)):
                b, a = y, x
                s = 0
                while True:
                    b, a = func(b, a)
                    if (c := 0 <= b < length and 0 <= a < width):
                        s += 1
                    if not c or int(data[b][a]) >= current:
                        dirs.append(s)
                        break
            p2 = max(p2, dirs[0] * dirs[1] * dirs[2] * dirs[3])
    print(p1)
    print(p2)