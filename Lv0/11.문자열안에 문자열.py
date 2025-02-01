def solution(str1, str2):

    if str2 in str1:
        return "포함되어 있습니다."
    else:
        return "포함되어 있지 않습니다."

str1 = input("문자열 입력: ")
str2 = input("확인하고 싶은 문자열 입력: ")

print(f"{str2}는 {str1}에 {solution(str1, str2)}")