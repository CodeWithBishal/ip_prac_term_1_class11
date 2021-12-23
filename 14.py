string = "0ABCD"
num = len(string)-1
i = 1
while i <= num :
    j = 1
    while j <= i:
        print(string[j], end = " ")
        j += 1
    print()
    i += 1