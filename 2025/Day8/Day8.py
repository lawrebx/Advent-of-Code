junctions = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y, z = (int(k) for k in line.split(','))
        junctions.append((x, y, z))

def dist2(j1, j2):
    return sum((j1[k] - j2[k])**2 for k in range(3))

union_map = {}
class Union:
    def __init__(self, members):
        self.members = members
        for m in members:
            union_map[m] = self
    def union(self, other):
        new_members = self.members | other.members
        return Union(new_members)

for p in junctions:
    Union({p})

all_pairs = []
for i, p in enumerate(junctions):
    for j in range(i+1, len(junctions)):
        q = junctions[j]
        all_pairs.append((p, q))
all_pairs.sort(key=lambda pair: dist2(pair[0], pair[1]))

part_1_cap = 1000

for i, (p, q) in enumerate(all_pairs):
    # part 1
    if i == (part_1_cap):
        unions = set()
        for p in junctions:
            unions.add(union_map[p])
        unions = list(sorted(unions, key=lambda u: len(u.members), reverse=True))
        print(len(unions[0].members) * len(unions[1].members) * len(unions[2].members))

    if union_map[p] == union_map[q]:
        continue
    u = union_map[p].union(union_map[q])
    
    # part 2
    if len(u.members) == len(junctions):
        print(p[0]*q[0])
        break