def importIsPossible(libraries, n):
    WHITE = 0
    GREY = 1
    BLACK = 2
    librariesColors = [WHITE] * (n+1)
    for i in range(1, n+1):
        wasGreyAlready = True
        if(librariesColors[i] == WHITE):
            wasGreyAlready = False
            librariesColors[i] = GREY
        print(librariesColors)
        if(libraries[i-1] != 0):
            for j in libraries[i-1]:
                if(librariesColors[j] == WHITE):
                    librariesColors[j] = GREY
                elif(librariesColors[j] == BLACK and wasGreyAlready):
                    return False
        librariesColors[i] = BLACK
    return True


libraries = [[3], [3], [4], [2]]
n = 4
if(importIsPossible(libraries, n)):
    print("SIM")
else:
    print("NAO")
