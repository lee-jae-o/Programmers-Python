def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, z = q.split()
        x, y, z = int(x), int(y), int(z)

        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        else:
            raise ValueError("오류: '+'나 '-' 연산자만 입력 가능합니다.")

        if result == z:
            answer.append('O')
        else:
            answer.append('X')

    return answer

x = input("첫 번째 정수 입력: ")
op = input("연산자 입력('+'나 '-'만 가능): ")
y = input("두 번째 정수 입력: ")
z = input("결과값 입력: ")

quiz = [f"{x} {op} {y} = {z}"]

try:
    print(solution(quiz))
except ValueError as e:
    print(e)
