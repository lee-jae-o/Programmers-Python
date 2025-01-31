def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])

    elif common[1] / common[0] == common[2] / common[1]:
        answer = common[-1] * (common[1] / common[0])

    return answer

user_input = input("등차수열 또는 등비수열을 입력하세요 (공백으로 구분): ")
common = list(map(int, user_input.split()))

print(f"{common}에서 {common[-1]}다음에 올 숫자는 {solution(common)}입니다.")