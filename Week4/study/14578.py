import sys
n = int(sys.stdin.readline())
dp = [0,1]
fac = 1
for i in range(3, n+1):
    dp[1], dp[0]= (i-1)*(dp[1]+dp[0])%1000000007, dp[1]
for i in range(1, n+1):
    fac *= i
    fac %= 1000000007
if n == 1: print(0)
else: print((fac * dp[1])% 1000000007)
# import sys
# n = int(sys.stdin.readline())
# dp = [0,1]
# fac = [1,2]
# if n > 2:
#     for i in range(3, n+1):
#         dp[1], dp[0]= ((i-1)*(dp[1]+dp[0])) % 1000000007, dp[1]
#         fac[1], fac[0] = i*fac[1], fac[1]
#     print((fac[1] * dp[1])% 1000000007)
# else:
#     print(fac[n-1] * dp[n-1])