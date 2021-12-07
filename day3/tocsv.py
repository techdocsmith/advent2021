with open("values.csv", "w+") as csv:   
    with open("./values.txt", "r") as values:
        for value in values.readlines():
            csv.write(",".join(list(value)))