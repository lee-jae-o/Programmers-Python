def solution(message):
    return len(message)*2

message = input("메세지를 입력하세요: ")
print(f"메세지를 적는데 필요한 최소 길이는 {solution(message)}cm 입니다.")