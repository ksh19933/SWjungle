x, y, w ,h = map(int, input().split(" "))
min_len = min(x, y, w-x, h-y)
print(min_len)


