input = '''1005162
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13'''

timestamp, trains = input.split("\n")

timestamp = int(timestamp)

trains = trains.split(",")

time_differences = []

for train in trains:
    if train == "x":
        time_differences.append(-1)
        continue
    train_divisor = int(train)
    closest_time = ((timestamp//train_divisor)*train_divisor)+train_divisor
    time_differences.append(closest_time-timestamp)

print(time_differences)

lowest = 999999999
index_of_lowest = 0

for index in range(0, len(time_differences)):
    if time_differences[index] < lowest and time_differences[index] != -1:
        index_of_lowest = index
        lowest = time_differences[index]

id_of_lowest = int(trains[index_of_lowest])
print(id_of_lowest*lowest)
