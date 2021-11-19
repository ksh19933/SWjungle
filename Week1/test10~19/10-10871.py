N, X = map(int, input().split(" "))
sen_num = list(map(int, input().split(" ")))
for i in range(N):
  if (sen_num[i] < X):
    print(sen_num[i], end=" ")