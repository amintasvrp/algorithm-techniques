n, m = map(int, raw_input().split())
press = 0

while(m > n):
    if(m % 2 == 1):
        m += 1
    else:
        m /= 2
    press += 1

press += n - m

print(press)
