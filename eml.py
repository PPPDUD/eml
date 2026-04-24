from math import log, exp

def eml(x, y):
    return exp(x) - log(y)


print("EML Machine Language interpreter version v0.1; copyright April 2026. Type h for help.")

ans = 0
while True:
    try:
        command = input(">").split()
    except EOFError:
        break
    try:
        if command[0] == "h":
            print("The syntax for invoking eml(x, y) is 'x y' without the quotes. If either argument is specified as ans, it will be substituted with the value from the previous operation (0 if no other operations have been run).")
            print("The special commands h and q show the help and exit, respectively. The interpreter will also exit upon receiving an end-of-file character.")
        elif command[0] == "q":
            break
        elif command[0] == "inv":
            ans *= -1
            print(ans)
        else:
            for index, i in enumerate(command):
                if i == "ans":
                    command[index] = ans
            ans = eml(float(command[0]), float(command[1]))
            print(ans)
    except Exception as e:
        print("Error!", e)