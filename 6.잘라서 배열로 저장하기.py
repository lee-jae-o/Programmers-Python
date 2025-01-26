def solution(my_str, n):
    answer = []

    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i + n])

    return answer

my_str = input("문자열을 입력하세요: ")
n = int(input("자르고 싶은 개수를 입력하세요: "))

print(solution(my_str, n))