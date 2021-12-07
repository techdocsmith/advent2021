#track distance units forward
y=0
#track depth
x=0
#track aim
z=0

input = "./moves.txt"
print("Using {input}".format(input=input))
with open(input, "r") as moves:
    for move in moves:
        print("Move: {move}".format(move=move))
        if move.split()[0]== "forward":
            x = x + int(move.split()[1])
            y = y + (z * int(move.split()[1]))
        elif move.split()[0]== "up":
            z = z - int(move.split()[1])
        elif move.split()[0]=="down":
            z = z + int(move.split()[1])


print ("Final y: {y}".format(y=y))
print ("Final x: {x}".format(x=x))
print ("Final z: {z}".format(z=z))
print ("x * y: {product}".format(product=(x*y)))