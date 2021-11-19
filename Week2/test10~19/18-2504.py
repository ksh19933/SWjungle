import sys
parenthses = sys.stdin.readline().strip()

#조건 1 올바른 괄호열 일 것
flag = 0
stack = []

for parenthsis in parenthses:
  if parenthsis == "(" or parenthsis == '[':
    stack.append(parenthsis)
    continue
  if parenthsis == ")": 
    if stack and stack[-1] == "(":
      stack.pop()
    else:
      flag = 1
      break
  if parenthsis == "]":
    if stack and stack[-1] == "[":
      stack.pop()
    else:
      flag = 1
      break

if stack or flag == 1:
  print(0)
else: 
  stack = []
  for parenthsis in parenthses:
    #조건2 "(" 혹은 "["일 경우 stack에 넣는다.
    if parenthsis == "(" or parenthsis == '[':
      stack.append(parenthsis)
      continue
    temp_sum = 1
    temp_stack = stack.pop()
    #조건3 ")"일 경우 temp_stack이 "("이면 2를 추가하고 아니면 temp_stack에 있는 숫자들을 더해준다. 그 후 결과물을 *2를 하고 다시 stack에 넣는다 ==> 중요한건 ")"가 들어왔으면 "("가 나올때까지 반복하는 것
    if parenthsis == ")":
      temp = 0
      if temp_stack == "(":
        stack.append(2)
      else:
        while(temp_stack != "("):
          temp += temp_stack
          temp_stack = stack.pop()
        stack.append(temp*2)
    #조건 4와 비슷한 방식으로 진행
    elif parenthsis == "]":
      temp = 0
      if temp_stack == "[":
        stack.append(3)
      else:
        while(temp_stack != "["):
          temp += temp_stack
          temp_stack = stack.pop()
        stack.append(temp*3)
    print(stack)
  print(sum(stack))

