def solution(my_string):
    return "".join(sorted(my_string.lower()))

my_string = input("정렬하고 싶은 문자열을 입력하세요: ")

print(f"정렬 결과: {solution(my_string)}")

