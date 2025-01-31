def solution(n, t):

    return n * (2 ** t)

n = int(input("처음 세균의 마리수를 입력하세요: "))
t = int(input("경과한 시간을 입력하세요 : "))

print(f"최종 증식한 세균의 마리수는 {solution(n, t)}마리 입니다.")