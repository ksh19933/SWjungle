import  sys
input = sys.stdin.readline

n = int(input())

if n >1:
    dp_fibo = [0, 0]
    dp_fibo[0] = 0
    dp_fibo[1] = 1
    i = 2
    while i <= n+1:
        tmp = dp_fibo.copy()
        dp_fibo[1] = (tmp[0]+tmp[1])%15746
        dp_fibo[0] = tmp[1]
        i += 1
    print(dp_fibo[1])
else:
    print(1)