# 옹알이(1)
def solution(babbling):
    possible_words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        original_word = word #디버깅 용
        for pw in possible_words:
            word = word.replace(pw, " ")

        if word.strip() == "":
            answer += 1

    return answer

user_input = input("조카가 말한 단어들을 공백으로 구분해서 입력하세요: ")

babbling_list = user_input.split()

result = solution(babbling_list)
print("조카가 발음할 수 있는 단어 개수:", result)
