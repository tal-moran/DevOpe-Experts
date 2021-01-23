

print(*range(5), sep=',')
star = '*'
i = 0
j = 6
for width in range(7):
    for length in range(7):
        if length == i or length == j:
            print("*", end="")
        else:
            print(" ", end="")

    print("")
    i += 1
    j -= 1
