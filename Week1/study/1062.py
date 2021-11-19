import sys
#재귀를 이용할 함수를 정의
#함수에는 배운 단어의 수와  K의 값이 같을 때  몇개의 단어를 읽을 수 있는지를 체크하는 함수를 호출
#함수에는 단어를 하나 뽑고 리스트에 저장한 후 다음 단어로 넘어가는 함수를 정의(백트래킹, for문, 재귀사용)

def dfs(depth, idx):
  global ctn
  if depth == K:
    temp_ctn = 0
    for word in words:
      temp_ctn += check_word(alphabets, word)
    if temp_ctn > ctn:
      ctn = temp_ctn
    return
  
  for i in range(idx, 123):
    if chr(i) not in alphabets:
      alphabets.append(chr(i))
      dfs(depth+1, i+1)
      alphabets.pop()
def check_word(alphabets, word):
  for c in word:
    if c not in alphabets:
      return 0 
  return 1

N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
#아스키 97~122
alphabets = ['a', 'n', 't', 'i', 'c']
ctn = 0
if K >= 5:
  dfs(5, 97)

print(ctn)