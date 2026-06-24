def equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    return ((-b + delta**0.5) / (2*a), (-b - delta**0.5) / (2*a))
