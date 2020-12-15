input = '''7,13,x,x,59,x,31,19'''

trains = input.split(",")

print(trains)

train_dict = {}

for index, train in enumerate(trains):
    if train != "x":
        train_dict[int(train)] = index

#start with the biggest ID so we aren't brute forcing for the next millenium
train_dict = dict(sorted(train_dict.items(), reverse=True))

attempt_index = 18115

base = None
base_offset = None


good = True

print(train_dict)

for key in train_dict:
    if not base:
        base = None
        base_offset = None
        base = key*attempt_index - train_dict[key]
        base_offset = train_dict[key]
    else:
        closest_to_base = ((base//key)*key) + key #closest departure to the base, but ahead by 1 instance (aka a bad ceiling funct lol)

        #if this is the correct timestamp, then this will be the same as base
        test = closest_to_base - train_dict[key]

        #this only applies if the offset is zero, which causes this strategy to break
        #needs to be decremented by one offset (the previous departure) to work properly
        if train_dict[key] == 0:
            test -= key
        
        print(f"for train ID {key} with offset {train_dict} | closest_to_base = {test}")

        if test == base:
            pass
            #continue
        else:
            good = False
            #break

if good:
    print(f"supposed solution: {base - base_offset}")
    #break
else:
    print(base)
    attempt_index += 1
    base = None
    base_offset = None
    #continue



#brute force pog lol

'''
attempt_index = 1

while True:
    base = attempt_index * int(trains[0]) #just whatever the first non "x" is
    print(base)
    good_attempt_index = True
    for index, element in enumerate(trains):
        if element == "x":
            continue
        else:
            element = int(element)
        if ((attempt_index*element) - index) == base:
            pass
        else:
            attempt_index += 1
            good_attempt_index = False
            break
    if good_attempt_index:
        print(base)
        break
'''