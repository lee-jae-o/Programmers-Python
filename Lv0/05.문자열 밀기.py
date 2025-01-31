def solution(A, B):

    if A == B:
        return 0

    for i in range(1, len(A)):
        A = A[-1] + A[:-1]
        if A == B:
            return i

    return -1

A = input("A에 들어갈 문자열을 입력하세요: ")
B = input("B에 들어갈 문자열을 입력하세요: ")

print(f"결과: {solution(A, B)}")