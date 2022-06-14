from itertools import combinations_with_replacement


def bruteForce(sentence, pattern):
    splitted = sentence.split()
    possiblePattern = combinations_with_replacement(pattern, 3)
    word1 = splitted[0]
    word2 = splitted[1]
    word3 = splitted[2]
    print(word1, word2, word3)
    print(pattern[0], pattern[1], pattern[2])

    for pattern in list(possiblePattern):
        if pattern[0] == pattern[1] and pattern[1] == pattern[2]:  # xxx, yyy, zzz
            if word1 == word2 and word2 == word3:
                print("String matched with pattern ", pattern)
            else:
                print("String not matched with pattern")
        elif pattern[0] != pattern[1] and pattern[0] == pattern[2]:  # xyx
            if word1 != word2 and word1 == word3:
                print("String matched with pattern ", pattern)
            else:
                print("String not matched with pattern")
        elif pattern[0] != pattern[2] and pattern[0] == pattern[1]:  # xxy
            if word1 != word3 and word1 == word2:
                print("String matched with pattern ", pattern)
            else:
                print("String not matched with pattern")
        elif pattern[0] != pattern[1] and pattern[1] == pattern[2]:  # xyy
            if word1 != word2 and word2 == word3:
                print("String matched with pattern ", pattern)
            else:
                print("String not matched with pattern")
        else:
            print("pattern melebihi batas variabel yang diizinkan")
