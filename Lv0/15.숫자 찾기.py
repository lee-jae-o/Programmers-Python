def solution(num, k):

    num_str = str(num)
    k_str = str(k)

    if k_str in num_str:
        return num_str.index(k_str) + 1

    else:
        return -1

num_str = input("num 입력: ")
num_k = input("k 입력: ")

print(f"{num_k}의 위치: {solution(num_str, num_k)}")