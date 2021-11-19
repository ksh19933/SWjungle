nums = input().split(" ")
A,B = [num[::-1] for num in nums]
num = A if (A>B) else B
print(num)