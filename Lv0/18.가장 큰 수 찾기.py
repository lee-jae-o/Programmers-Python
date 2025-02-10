def solution(array):
    return [max(array), array.index(max(array))]

user_input = input("정수 배열을 공백으로 구분하여 입력하세요: ")
array = list(map(int, user_input.split()))

result = solution(array)
print(result)