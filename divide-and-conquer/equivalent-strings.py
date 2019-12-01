def mergesort(string):
    if(len(string) % 2 == 1):
        return string
    else:
        middle = round(len(string) / 2)
        stringA = mergesort(string[0: middle])
        stringB = mergesort(string[middle:])
        if(stringA < stringB):
            return (stringA + stringB)
        else:
            return (stringB + stringA)


stringA = input()
stringB = input()

if(mergesort(stringA) == mergesort(stringB)):
    print("YES")
else:
    print("NO")
