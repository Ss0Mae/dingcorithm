input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array=[]
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]

        if alphabet_occurence == 1:
            not_repeating_character_array.append(chr(index+ord("a")))
        # 빈도수 1인 애들 알파벳 위치 인덱스에다가 집어 넣었음

    for char in string:
        if char in not_repeating_character_array:
            return char # 앞에서 부터 순회하면서 답 찾으면 바로 리턴


    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))