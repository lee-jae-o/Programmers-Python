def solution(num, total):

    if total % num != num * (num - 1) // 2 % num:
        return "해당하는 연속된 숫자가 없습니다"

    answer = []
    start = (total - (num * (num - 1) // 2)) // num
    for i in range(num):
        answer.append(start + i)
    return answer

num = int(input("연속된 숫자의 개수를 입력하세요: "))
total = int(input("총합을 입력하세요: "))

result = solution(num, total)
print("연속된 숫자 리스트:", result)