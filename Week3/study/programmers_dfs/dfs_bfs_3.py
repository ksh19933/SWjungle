from collections import deque
def solution(begin, target, words):
  answer = 0
  n = len(words)
  word_n = len(begin)
  que = deque([[begin, 0]])
  while que:
    case, cnt = que.popleft()
    if case == target:
      answer = cnt
      break 
    if cnt < n:
      for word in words:
        change = 0
        for i in range(word_n):
          if case[i] != word[i]:
            change += 1
        if change == 1:
          que.append([word, cnt+1])

  return answer

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))