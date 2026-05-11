def reverse(text):
    array = []
    for i in range(len(text)):
        i += 1
        array.append(text[-i])
    result = ''.join(array)
    return result
