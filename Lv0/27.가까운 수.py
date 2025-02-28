def solution(array, n):
    return min(array, key=lambda x: (abs(x - n), x))

array = list(map(int, input("정수 리스트 입력 (공백으로 구분): ").split()))
n = int(input("원하는 수 입력: "))

print(solution(array, n))
