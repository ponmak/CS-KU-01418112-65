# 01 Count English Characters

def count_char(word) -> dict:
    result = {}
    for ch in word:
        ch = ch.lower()
        if ch.isalpha():
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result

print(count_char('Hello, There'))