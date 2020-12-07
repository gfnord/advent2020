# Read the input
lines = [x.strip() for x in open('input.txt', 'r').readlines()]
bags = {}

for x in lines:
    bag, contains = x.split('contain')
    bag = bag.replace(' bags','')
    bags[bag] = contains

def deeps(bag, bags):
    contains = []
    for b in bags:
        if bag in bags[b]:
            contains.append(b)
            contains.extend(deeps(b, bags))
    return set(contains) # use set to remove duplicates

print("bags: ", len(deeps('shiny gold', bags)))
