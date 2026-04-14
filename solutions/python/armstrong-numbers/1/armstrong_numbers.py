def is_armstrong_number(number):
    len_number = len(str(number))
    result = 0
    for i in range(len_number):
        result += int(str(number)[i]) ** len_number
    return number == result
