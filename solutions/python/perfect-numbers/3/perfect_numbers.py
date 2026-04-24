def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    half = number // 2
    sum = 0
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    while half > 0:
        if number % half == 0:
            sum += half
            half -= 1
        else:
            half -= 1
        if sum > number:
            return 'abundant'

    if sum < number:
        return 'deficient'
        
    return 'perfect'
