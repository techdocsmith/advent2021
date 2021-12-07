
oldsum = 0
index = 0
increased = 0
with open ("./inputs.txt", "r") as values:
    lines = values.readlines()
    for line in lines:
        # Don't take a sum until the first window
        if index > 1:
            val1 = int(lines[index].strip())
            val2 = int(lines[index - 1].strip())
            val3 = int(lines[index - 2].strip())
            mysum = val1 + val2 + val3
            # Don't start comparing values until the 2nd window
            if index > 2:
                if mysum > oldsum:
                    print("{sum} increased [{oldsum}]".format(sum=mysum, oldsum=oldsum))
                    increased += 1
                elif mysum == oldsum:
                    print("{sum} no change [{oldsum}]".format(sum=mysum, oldsum=oldsum))
                else:
                    print("{sum} decreased [{oldsum}]".format(sum=mysum, oldsum=oldsum))
            oldsum=mysum
        else:
            print("(N/A - no previous sum)")
        index +=1

print("Increased amount: {increased}".format(increased=increased))

    