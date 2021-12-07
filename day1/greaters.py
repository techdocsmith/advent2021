
oldval = None
increased = 0
with open ("./inputs.txt", "r") as values:
    lines = values.readlines()
    for line in lines:
        if oldval != None:
            #print("got an old value {oldval}".format(oldval=oldval))
            if int(line.strip()) > oldval:
                print("({newval}) increased [{oldval}]".format(newval=line.strip(), oldval=oldval))
                increased += 1
        else:
            print("(N/A - no previous measurement)")
        oldval=int(line.strip())

print("Increased amount: {increased}".format(increased=increased))

    