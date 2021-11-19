import sys
N = int(sys.stdin.readline())
liquid_features = list(map(int, sys.stdin.readline().split()))
liquid_features.sort()
print(liquid_features)
pl = 0
pr = N - 1
min = sys.maxsize
while pl < pr:
  temp_feature = liquid_features[pr] + liquid_features[pl]
  if abs(temp_feature) < min:
    liquid1 = liquid_features[pl]
    liquid2 = liquid_features[pr]
    min = abs(temp_feature)
  if temp_feature < 0:
    pl += 1
  else:
    pr -= 1

print(f'{liquid1} {liquid2}')
  

