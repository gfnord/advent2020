# Read the input
lines = [x.strip() for x in open('input.txt', 'r').readlines()]
bags = {}
q = []

for l in lines:
    l = l.replace('bags', '').replace('bag', '').replace('.','') # remove bags, bag and dots
    bag, contains = l.split('contain')
    bag = bag.strip()

    if 'no other' in contains: 
        bags[bag] = {}
        continue

    contains = contains.split(',')
    contain_dict = {}
    for c in [c.strip() for c in contains]:
        amount = c[:2]
        color = c[2:]
        contain_dict[color] = int(amount)
    bags[bag] = contain_dict


def Count(bag, bags): # recursive count function
    count = 1  # Count the bag itself
    contained_bags = bags[bag]
    for c in contained_bags:
        multiplier = contained_bags[c]
        count += multiplier * Count(c, bags)
    return count


answer = Count('shiny gold', bags) - 1 # do not count itself
print('Answer: ', answer)
