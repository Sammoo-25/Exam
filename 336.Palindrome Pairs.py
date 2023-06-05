def is_palindrome(word):
    return word == word[::-1]

def palindromePairs(words):
    word_dict = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if reversed_prefix in word_dict and word_dict[reversed_prefix] != i and is_palindrome(suffix) and suffix != "":
                result.append([i, word_dict[reversed_prefix]])

            if reversed_suffix in word_dict and word_dict[reversed_suffix] != i and is_palindrome(prefix):
                result.append([word_dict[reversed_suffix], i])

    return result

words = ["abcd", "dcba", "lls", "s", "sssll"]
output = palindromePairs(words)
print(output)
