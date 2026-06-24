import numpy as np

def posicao_mru(s0, v, t):
    return s0 + v * t


def gerar_dados(s0, v, tempo_final, passos=100):
    t = np.linspace(0, tempo_final, passos)
    s = posicao_mru(s0, v, t)
    return t, s
