input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

bag_rules = input.split("\n")

#{"adjective color": [[int, "adjective color"], ...], ... }
bag_dict = {}

for bag_rule in bag_rules:
    words = bag_rule.split(" ")
    #first two words are always the bag type
    bag_type = words[0] + " " + words[1]

    #fifth word determines if this is a dead end or not
    if words[4] == "no":
        bag_dict[bag_type] = []
    else:
        #children bag types always come in groups of four, so we can just parse the number and type
        #from the first three words of each group
        #they also start coming after the first four words, which is the bag_type
        children_types_count = int((len(words)-4)/4)
        children_types = []
        for i in range(0, children_types_count):
            group_start_index = (4*i)+4
            children_type = words[group_start_index+1] + " " + words[group_start_index+2]
            children_count = int(words[group_start_index+0])
            children_types.append([children_count, children_type])
        bag_dict[bag_type] = children_types


def gold_bag_finder(bag_type):
    '''recursive function to hunt down "shiny gold" end-rules
    
    if a rule ends in a dead end, then this function returns False; if ANY
    part of the recursion tree returns True, then this function returns True.

    i've assumed that all bags always end in dead ends somewhere
    '''
    rules = bag_dict[bag_type]
    print(f"{bag_type} - {rules}")
    if not rules:
    #dead end
        return False
    for rule in rules:
        if rule[1] == "shiny gold":
            return True
    #none of the rules for this bag directly lead to a shiny gold bag
    #so we will need to test each child rule with this method
    #if all of them come up as dead ends, then we return False
    #but if one of them comes up a not dead end, then we return True
    #if a child returns True (by a direct "shiny gold" find), then every parent will return True
    #if a child returns False, parents will go to the next rule; if all rules
    #are exhausted and there still isn't a good end, we give up
    good_end_found = False
    for rule in rules:
        output = gold_bag_finder(rule[1])
        if output:
            good_end_found = True
            return True
    #it's implied there isn't a good end here
    return False
        
valid_rules = 0    

for bag_type in bag_dict:
    print("-------")
    print(f"{bag_type} - {bag_dict[bag_type]}")
    children_bags = bag_dict[bag_type]
    for child_bag in children_bags:
        #check if a first child bag can directly hold a shiny gold
        #this isn't checked by the recursive funct oops lol
        if child_bag[1] == "shiny gold" or gold_bag_finder(child_bag[1]):
            print("^!^!^!^!^!^!^!^!^!^!^!^")
            valid_rules += 1
            #once we've decided the highest-level of bag has some valid end
            #STOP
            break

print(valid_rules)

