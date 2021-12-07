import numpy

oxygen = []
co2 = []
oxygen_val = 0
co2_val = 0




#file = "./examples.txt"
file = "./values.txt"

# Build 2 lists of lists to reduce
with open(file, "r") as values:
    linelist = values.readlines()
    length = len(linelist)
    for value in linelist:
        # Remove pesky newline
        value = value.strip()
        #print(value.strip())
        # Convert to list
        split = list(value)
        # Convert list items to int
        split = list(map(int, split))
        oxygen.append(split)
        co2.append(split)
        # Add the lists
        #totals = numpy.add(totals, split)

# Reduce oxygen
# Need to do the procedure 1 time for each column
for x in range(len(oxygen[0])):
    # Find most commmon in column x
    length = len(oxygen)
    total = 0
    common = 0
    print(length)
    if length > 1:
        for value in oxygen:
            total = total + value[x]
        #print("Total: {total}".format(total=total))
        if total >= length/2:
            common=1
        # Go through oxygen again and remove values that don't match
        new_oxygen = []
        for value in oxygen:
            #print("Comparing common {common} and value[{x}]".format(common=common, x=x))
            #print("Value: {value}".format(value=value))
            if value[x] == common:
                #print("Removing {value}".format(value=value))
                new_oxygen.append(value)
        oxygen = new_oxygen
        #print("Current oxygen: {oxygen}".format(oxygen=oxygen))
print("Oxygen: {oxygen}".format(oxygen=oxygen))

# Reduce CO2
# Need to do the procedure 1 time for each column
for x in range(len(co2[0])):
    # Find most commmon in column x
    length = len(co2)
    total = 0
    common = 0
    if length > 1:
        for value in co2:
            total = total + value[x]
        print("Total: {total}, length: {length}".format(total=total, length=length))
        if total > length/2:
            common=0
        elif total < length/2:
            common=1
        # Go through oxygen again and remove values that don't match
        new_co2 = []
        for value in co2:
            #print("Comparing common {common} and value[{x}]".format(common=common, x=x))
            #print("Value: {value}".format(value=value))
            if value[x] == common:
                #print("Removing {value}".format(value=value))
                new_co2.append(value)
        co2 = new_co2
        #print("Current CO2: {co2}".format(co2=co2))
print("CO2: {co2}".format(co2=co2))




# Calculate the values
my_oxygen = oxygen[0]
my_oxygen.reverse()
print(my_oxygen)
for idx, val in enumerate(my_oxygen):
    print(val*(2**idx))
    oxygen_val =  oxygen_val + val*(2**idx)
    print(oxygen_val)
print("Oxygen val: {oxygen_val}".format(oxygen_val=oxygen_val))

my_co2=co2[0]
my_co2.reverse()
for idx, val in enumerate(my_co2):
    co2_val = co2_val + val*(2**idx)
print("CO2 val {co2_val}".format(co2_val=co2_val))

print("LSR: {lsr}".format(lsr=oxygen_val*co2_val))



