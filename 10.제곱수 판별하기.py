def solution(n):
    a = n ** (1 / 2)
    if a % 1 == 0:
        return "제곱수가 맞습니다."
    else:
        return "제곱수가 아닙니다."

n = int(input("판별하고 싶은 정수를 입력하세요: "))

print(f"{n}: {solution(n)}")