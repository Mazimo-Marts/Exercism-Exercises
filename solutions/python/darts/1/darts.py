def score(x, y):
    ponto = (x**2 + y**2) ** 0.5
    if ponto > 10:
        return 0
    elif ponto > 5:
        return 1
    elif ponto > 1:
        return 5
    else:
        return 10
 