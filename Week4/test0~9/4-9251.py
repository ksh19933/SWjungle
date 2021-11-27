import sys

str1 = [0] + list(sys.stdin.readline().strip())
str2 = [0] + list(sys.stdin.readline().strip())
arr = [[0] * (len(str2)) for _ in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            arr[i][j] += arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[len(str1)-1][len(str2)-1])