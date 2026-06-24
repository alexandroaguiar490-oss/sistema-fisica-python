import numpy as np


def posicao_mruv(velocidade_inicial, aceleracao, tempo):
    return velocidade_inicial * tempo + 0.5 * aceleracao * tempo ** 2


def gerar_dados_mruv(velocidade_inicial, aceleracao, tempo_final, passos=100):
    t = np.linspace(0, tempo_final, passos)
    s = posicao_mruv(velocidade_inicial, aceleracao, t)
    return t, s
