# Kelsier é um motoboy que trabalha entregando pizzas para uma pizzaria, no
# entanto, recentemente a pizzaria vem recebendo muitas reclamações de alguns
# pedidos que demoram a chegar. Então, a pizzaria decidiu que Kelsier passaria a
# entregar os pedidos que demorassem mais a serem entregues, primeiro. Ou seja,
# supondo que a pizzaria diga que Kelsier deva entregar no máximo 10 pizzas, dentre
# os pedidos que a pizzaria recebeu, sendo esses; 5 pizzas que demoram 15 min
# para serem entregues; 4 pizzas que demoram 23 minutos para serem entregues; 2
# pizzas que demoram 21 min; 4 pizzas que demoram 16 min; 5 pizzas que demoram
# 19 min; e 2 pizzas que demoram 18 min para serem entregues. Sendo assim,
# Kelsier deve entregar as pizzas de forma que não extrapole a quantidade máxima
# (10) estipulada pela pizzaria, maximizando o tempo de entrega. Logo, Kelsier
# entregaria as 4 pizzas que demoram 23 min, as 2 pizzas que demoram 21 min e as
# 2 pizzas que demoram 18 min, totalizando 8 pizzas entregues em 62 min.
# Escreva uma solução para ajudar Kelsier a saber quanto tempo ele levará
# para entregar os pedidos mais demorados.



def matrix(packages, maxTime):
    amount = [x[1] for x in packages]
    time = [x[0] for x in packages]
    matrix = [[0] * (maxTime+1) for i in range(len(amount)+1)]
    for i in range(1, len(amount)+1):
        for j in range(1, maxTime + 1):
            if(j < amount[i-1]):
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], time[i-1] + matrix[i-1][j-amount[i-1]])
    
    # for i in range(len(matrix)): print(matrix[i])
    
    return matrix

def minutes(packages, maxTime):
    packages = sorted(packages, key=lambda element: (element[1], element[0]), reverse=True)
    result = matrix(packages, maxTime)
    return result[-1][-1]

def pizzas(packages, maxTime):
    packages = sorted(packages, key=lambda element: (element[1], element[0]), reverse=True)
    amount = [x[1] for x in packages]
    time = [x[0] for x in packages]

    matrixMinutes = matrix(packages, maxTime)
    i = len(matrixMinutes) - 1
    j = len(matrixMinutes[0]) - 1
    packages = []

    while(matrixMinutes[i][j] != 0):
        if(matrixMinutes[i][j] == matrixMinutes[i-1][j]):
            i = i - 1
        else:
            packages.append((time[i-1], amount[i-1]))
            j = j - amount[i-1]
            i = i - 1
    
    return packages
        
packages = [(14, 4), (21,2),(26,7),(18,4),(30,13),(10,2)]
n = 7
print(pizzas(packages,n)) 
print(minutes(packages,n))