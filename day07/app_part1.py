# Read the input
lines = [x.strip() for x in open('input.txt', 'r').readlines()]
bags = {}

for x in lines:
    bag, contains = x.split('contain')
    bag = bag.replace(' bags','')
    bags[bag] = contains

def deeps(fbag, fbags):
    fcontains = []
    for b in fbags:
        if fbag in fbags[b]:
            fcontains.append(b)
            fcontains.extend(deeps(b, fbags))
    return set(fcontains) # use set to remove duplicates

print("bags: ", len(deeps('shiny gold', bags)))
