def solution(n):
    return sum(map(int, str(n)))

n = int(input("정수를 입력하세요: "))

print(f"입력한 n의 각 자리 정수 합: {solution(n)}")