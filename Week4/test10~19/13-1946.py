import sys
input = sys.stdin.readline

test_num = int(input())
for _ in range(test_num):
    people_num = int(input())
    scores = [list(map(int, input().split())) for _ in range(people_num)]
    scores.sort()
    min_srd = scores[0][1]
    stack = []
    print(scores)
    for i in range(people_num):
        if min_srd >= scores[i][1]:
            min_srd = scores[i][1]
            stack.append(scores[i])
    print(len(stack))