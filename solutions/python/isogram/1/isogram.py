def is_isogram(string):
    count = []
    string = "".join(letter for letter in string if letter.isalpha()).lower()
    for letter in string:
        if letter in count:
            return False
        count.append(letter)
    return True