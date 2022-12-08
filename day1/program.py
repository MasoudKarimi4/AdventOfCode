from input import collection

# Part One
numList = collection
collection = collection.split("\n")
lists = []
empty = []
for g in collection:
    if g == '':
        lists.append(empty)
        empty = [] 
    else:
        empty.append(g)

biggest = 0


for g in range(len(lists)):
    add = 0
    for p in range(len(lists[g])):
        add += int(lists[g][p])
    if add > biggest:
        biggest = add

# Part Two
intList = []
for g in collection:
    if g == '':
        continue
    else:
        intList.append(int(g))

print(sorted(intList))


print(57301+ 64480+ 66601)