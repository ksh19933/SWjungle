import math
a, b, v = list(map(int, input().split(" ")))
d = math.ceil((v-b)/(a-b))
print(d)