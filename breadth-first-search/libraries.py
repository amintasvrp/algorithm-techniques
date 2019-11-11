# Vin é uma programadora e precisa importar algumas bibliotecas em seu
# código. Após pesquisar um pouco, ela descobre que algumas bibliotecas dependem
# de outras bibliotecas, que, por sua vez, necessitam de outras bibliotecas e assim
# por diante.
# Vin chegou a uma lista final com todas as bibliotecas que precisará. Com
# essa lista em mãos, ela suspeita que a mesma possui loops. Por exemplo, se uma
# biblioteca A depende de outra biblioteca B, que por sua vez depende da biblioteca
# A, tornaria a tarefa interminável.
# Dada a lista de dependência entre as bibliotecas, implemente um algoritmo
# que determina se Vin conseguirá ou não importar todas as bibliotecas.
# Como entrada você receberá um n, que equivale ao número de bibliotecas,
# enumeradas de 1 até n, e um array simbolizando as dependências.
# Exemplo: [[2],0,[1]], o qual diz que a biblioteca 1 depende da biblioteca 2, a
# biblioteca 2 não depende de nenhuma outra, e a biblioteca 3 depende da biblioteca
# 1. Sua solução deve dizer SIM caso Vin consiga importar todas as bibliotecas e
# NAO caso contrário.

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


libraries = [[3],[3],[4],[2]]
n = 4
if(importIsPossible(libraries, n)):
    print("SIM")
else:
    print("NAO")