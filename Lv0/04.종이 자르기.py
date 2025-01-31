def solution(M, N):

    answer = M * N - 1

    return answer

M = int(input("가로 길이를 입력 하세요: "))
N = int(input("세로 길이를 입력 하세요: "))

print(f"가로의 길이가 {M}이고, 세로의 길이가 {N}일 때, 최소 가위질 횟수는 {solution(M, N)}번 입니다.")