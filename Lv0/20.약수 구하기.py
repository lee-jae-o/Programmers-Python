def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

n = int(input("정수 입력: "))
print(f"{n}의 약수는 {solution(n)} 입니다.")