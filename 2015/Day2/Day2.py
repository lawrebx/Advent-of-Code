import sys, os
             
input_file = os.path.dirname(sys.argv[0])+'/input.txt'

with open(input_file) as f:
    gift_list = [[int(i) for i in line.rstrip().split('x')] for line in f]

################################ PART ONE ################################
"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. 
They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
The elves also need a little extra paper for each present: the area of the smallest side.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

"""

def get_surface_area(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    sides = [l*w,w*h,h*l]
    extra = min(sides)
    surface_area = sum(2*sides) + extra

    return surface_area

total_area = sum([get_surface_area(gift) for gift in gift_list])

print(f'How many total square feet of wrapping paper should they order?\nAnswer: {total_area} square feet.')   

################################ PART TWO ################################
"""
The ribbon required to wrap a present is the shortest distance around its sides, 
or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; 
the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?

"""
from functools import reduce


def get_ribbon_footage(dimensions):

    dimensions.sort(reverse=False)
    wrap = dimensions[0] * 2 + dimensions[1] * 2
    bow = reduce(lambda x, y:x * y, dimensions)

    total_ribbon = wrap + bow

    return total_ribbon

total_ribbon = sum([get_ribbon_footage(gift) for gift in gift_list])

print(f'How many total feet of ribbon should they order?\nAnswer: {total_ribbon} feet.')   