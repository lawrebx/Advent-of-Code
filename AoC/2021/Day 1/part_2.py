"""
--- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

"""

from depthcheck import depthCheck

#Read raw input from text file in directory
#Convert to int and check for error types
with open('input.txt') as f:
    input_raw = f.readlines()

try:
    observations_raw = [int(item) for item in input_raw]
except ValueError as error:
    print(error)
    print("Could not convert input data to integer. Check input data types. The program will now close.")
    exit()

#Observational group logic
#I want to access sums of groups

observations = []

for k in range(0, len(observations_raw)-2):
    group_depth = observations_raw[k] + observations_raw[k + 1] + observations_raw[k + 2]
    observations.append(group_depth)

#Reuse comparison code from Part 1
i=0

depth_change_list = []

for depth in observations:
    if i == 0:
        depth_change = 0
    elif i > 0:
        prev_depth = observations[i - 1]
        current_depth = observations[i]
        depth_change = depthCheck(prev_depth,current_depth)
        
    depth_change_list.append(depth_change)
    i = i + 1

increase_count = sum(map(lambda x : x == 1, depth_change_list))

print(f'{increase_count} observations were greater than the previous.')


