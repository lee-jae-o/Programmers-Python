def solution(array):
    answer = 0

    for i in array:
        answer += str(i).count("7")

    return answer

array = list(map(int, input("array에 들어갈 숫자를 입력하세요: ").split()))

print(solution(array))