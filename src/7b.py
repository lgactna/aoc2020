input = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

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
    '''recursive function based on 7a's
    '''
    rules = bag_dict[bag_type]
    print(f"{bag_type} - {rules}")
    if not rules:
    #dead end
        return None
    for rule in rules:
        base_count = rule[0] #includes the containing bags themselves
        child_output = gold_bag_finder(rule[1])
        if not child_output:
            #that's a dead end, just return the number of dead-end bags
            return rule[0]
        else:
            #not a dead end; return the number of children times this bag type
            return (rule[0]*child_output)+rule[0]

#we can always start with bag_dict["shiny gold"]
#so we just modify the magic recursion function to return the count of children

print(gold_bag_finder("shiny gold"))
