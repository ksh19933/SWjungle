# N, M = map(int, input().split())		# 금액, 기업 수 입력
# byInvestment = [[0 for _ in range(M + 1)]]	# 기업 투자금액별 수익금 저장 리스트.

# for _ in range(N):				# 기업별 수익금 데이터 추가
#     byInvestment.append(list(map(int, input().split())))
# print(byInvestment)
# # 최대 이익 계산할 테이블
# table = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# # 최대 이익시 투자할 기업을 추적할 테이블
# pos = [[[0 for _ in range(M+1)] for _ in range(M + 1)] for _ in range(N+1)]

# for i in range(1, N + 1):			# 행, 투자금
#     for j in range(1, M + 1):			# 열, 기업
#         # table[i][j]에 이전기업까지 고려했을 때의 최댓값과 현재 기업에 모든 돈을 투자한 경우 중 최댓값 대입
#         table[i][j] = max(table[i][j-1], byInvestment[i][j])
#         if table[i][j] == byInvestment[i][j]:	# 만약 현재 기업에 모두 투자하는 것이 이익이 더 크다면
#             pos[i][j][j] = i			# 방법 추적
#         else:					# 이전기업까지 고려한 경우가 더 크다면
#             pos[i][j] = pos[i][j-1].copy()	# 이전기업까지 고려한 것을 복사
            
#         # 현재 기업 소량 분산투자하는 경우 (이전 기업 투자 최댓값 + 현재 기업 투자)
#         for k in range(1, i+1):
#             # 만약 현재 table[i][j] 값보다 이전 기업들 + 현재 기업 투자하는 것이 더 크다면
#             if table[i][j] < table[k][j-1] + byInvestment[i-k][j]:
#                 # 값 대입
#                 table[i][j] = table[k][j-1] + byInvestment[i-k][j]
#                 pos[i][j] = pos[k][j-1].copy()	# 이전 방법 복사
#                 pos[i][j][j] = i-k		# 현재 기업 투자금 추가
#     print(table)
# # 출력
# print(table[-1][-1])
# print(*pos[-1][-1][1:])


import copy
n, m = map(int, input().split())

# i번째 기업에 j 원을 투자했을 때 얻는 금액
invest = [[0] for _ in range(m)]
for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(1, len(l)):
        invest[i-1].append(l[i])
print(invest)

dp = [0 for _ in range(n+1)]
path = [[] for i in range(n+1)]

for i in range(n+1):
    dp[i] = invest[0][i]
    path[i].append(i)
print(dp)
print(path)
for i in range(1, m): # 2번째 기업부터 모든 기업에 대해 반복
    for j in range(n, -1, -1): # 해당 기업의 바로 전단계까지의 누적 투자 금액에 대해 거꾸로 반복
        add = 0
        for k in range(1, j+1): # 해당 누적 투자 금액에서 이 기업에 투자해서 얻는 이득 갱신
            if dp[j-k] + invest[i][k] > dp[j]:
                dp[j] = dp[j-k] + invest[i][k]
                path[j] = copy.deepcopy(path[j-k])
                add = k
        path[j].append(add)

print(dp[-1])
print(*path[-1])