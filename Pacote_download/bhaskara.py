def formula_bhaskara(a, b, c):
    """
    Programa que recebe 3 valores e realiza a fórmula de Bháskara
    e retorna o delta e x1 e x2
    :param a: Valor equivalente ao a da função de segundo grau
    :param b: Valor equivalente ao b da função de segundo grau
    :param c: Valor equivalente ao c da função de segundo grau
    :return: (delta, x1, x2)
    """
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        x1 = ((-b) + delta ** (1 / 2)) / (2 * a)
        x2 = ((-b) - delta ** (1 / 2)) / (2 * a)
        return delta, x1, x2
    else:
        return "Valor não pertencente aos números reais"
