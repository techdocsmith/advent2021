#track distance units forward
y=0
#track depth
x=0

with open("./moves.txt", "r") as moves:
    for move in moves:
        print("Move: {move}".format(move=move))
        if move.split()[0]== "forward":
            distance = int(move.split()[1])
            print("Adding {distance} to {y}".format(y=y, distance=distance))
            y = y + distance
        elif move.split()[0]== "up":
            x = x - int(move.split()[1])
        elif move.split()[0]=="down":
            x = x + int(move.split()[1])

print ("Final y: {y}".format(y=y))
print ("Final x: {x}".format(x=x))
print ("x * y: {product}".format(product=(x*y)))