def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    return "".join(my_list)

my_string = input("문자열 입력: ")
num1 = int(input("num1 입력: "))
num2 = int(input("num2 입력: "))

print(solution(my_string, num1, num2))
