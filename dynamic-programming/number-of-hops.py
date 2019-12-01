def min_jumps_for_each_position(jumps):
    size = len(jumps)
    min_jumps = [0] * size
    for i in range(size-2, -1, -1):
        if(i + jumps[i] >= size):
            min_jumps[i] = 1
        else:
            minimal_jumps = min_jumps[i+1]
            for j in range(i+2, jumps[i] + 1):
                if(min_jumps[j] < minimal_jumps):
                    minimal_jumps = min_jumps[j]
            min_jumps[i] = minimal_jumps + 1
    return min_jumps


def min_jumps(jumps):
    result = min_jumps_for_each_position(jumps)
    return result[0]


def find_jumps(jumps):
    min_jumps_position = min_jumps_for_each_position(jumps)
    route = [jumps[0]]
    minimal = min_jumps_position[0]
    i = 0
    while i < len(min_jumps_position) - 1:
        if(min_jumps_position[i] <= 1):
            route.append(jumps[i])
            break
        elif(min_jumps_position[i] < minimal):
            route.append(jumps[i])
            minimal = min_jumps_position[i]
        i += 1
    route.append(jumps[-1])
    return route


jumps = list(map(int, input().split()))
print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(find_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
