import sys
input = sys.stdin.readline

multi_num, device_num = map(int, input().split())
devices = list(map(int, input().split()))

tap = [0] * multi_num
i = max_i = cnt = 0
for device in devices:
    if device in tap:
        pass
    elif 0 in tap:
        tap[tap.index(0)] = device
    else:
        for fl in tap:
            if not devices[i:].count(fl):
                tmp = fl
                break
            elif devices[i:].index(fl) > max_i:
                tmp = fl
                max_i = devices[i:].index(fl)
        tap[tap.index(tmp)] = device
        max_i = 0
        cnt += 1
    i += 1
print(cnt)