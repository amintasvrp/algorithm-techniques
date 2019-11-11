# Equivalent Strings

# Today on a lecture about strings Gerald learned a new definition of string equivalency. 
# Two strings a and b of equal length are called equivalent in one of the two cases:
# 1. They are equal.
# 2. If we split string a into two halves of the same size a1 and a2, and string b into two halves of the same size b1 and b2, then one of the following is correct:
#   2.1. a1 is equivalent to b1, and a2 is equivalent to b2
#   2.2. a1 is equivalent to b2, and a2 is equivalent to b1
# As a home task, the teacher gave two strings to his students and asked to determine if they are equivalent.

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
