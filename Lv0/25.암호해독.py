def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

cipher = input("암호 입력: ")
code = int(input("코드 입력: "))
print(f"해독된 암호: {solution(cipher, code)}")