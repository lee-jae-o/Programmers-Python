def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

answer = input("문자열 입력: ")
print(solution(answer))