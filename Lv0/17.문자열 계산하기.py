def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])

    for i in range(len(my_string)):
        if my_string[i] == '+':
            answer += int(my_string[i + 1])
        elif my_string[i] == '-':
            answer -= int(my_string[i + 1])
        else:
            continue

    return answer

my_string = input("계산하고 싶은 문자열 입력(숫자와 연산자는 공백으로 구분): ")
print(solution(my_string))