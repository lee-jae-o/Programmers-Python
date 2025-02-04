def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

numlist = list(map(int, input("배열을 입력하세요 (숫자를 공백으로 구분): ").split()))
n = int(input("n을 입력하세요:"))

print(solution(n,numlist))