def solution(s1, s2):

    answer = 0

    for i in s1:
        if i in s2:
            answer += 1

    return answer

s1 = input("s1을 입력하세요: ").split()
s2 = input("s2을 입력하세요: ").split()

print(f"종복된 원수 개수는 {solution(s1,s2)}개 입니다.")
