from sys import argv

for i in argv[1:]:
    f = open(i, "r")
    parsed = f.read().split("\n")
    f.close()
    for index, j in enumerate(parsed):
        if j:
            if j[0] == "!":
                print(j)
                g = open(j[1:])
                parsed[index] = g.read()
                g.close()
    f = open(i, "w")
    f.write("\n".join(parsed))
    f.close()
