import numpy

totals = [0,0,0,0,0,0,0,0,0,0,0,0]
length = 0
gamma_val = 0
epsilon_val = 0



#file = "./examples.txt"
file = "./values.txt"

with open(file, "r") as values:
    linelist = values.readlines()
    length = len(linelist)
    for value in linelist:
        # Remove pesky newlinew
        value = value.strip()
        #print(value.strip())
        # Convert to list
        split = list(value)
        # Convert list items to int
        split = list(map(int, split))
        # Add the lists
        totals = numpy.add(totals, split)

print("Totals: {totals}".format(totals=totals))
print("List length: {length}".format(length=length))

# Take the totals and halve them
def greater(n):
    if n > length/2:
        return 1
    else:
        return 0

gamma = list(map(greater, totals))
print("Gamma: {gamma}".format(gamma=gamma))

def switch(n):
    if n== 0:
        return 1
    else: return 0

epsilon = list(map(switch, gamma))
print("Epsilon: {epsilon}".format(epsilon=epsilon))


# Calculate the values
gamma.reverse()
for idx, val in enumerate(gamma):
    gamma_val = gamma_val + val*(2**idx)
print("Gamma val: {gamma_val}".format(gamma_val=gamma_val))

epsilon.reverse()
for idx, val in enumerate(epsilon):
    epsilon_val = epsilon_val + val*(2**idx)
print("Epsilon val {epsilon_val}".format(epsilon_val=epsilon_val))

print("Consupmption: {consumption}".format(consumption=gamma_val*epsilon_val))



