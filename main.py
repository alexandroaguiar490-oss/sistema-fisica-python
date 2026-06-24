from simulacoes.mru import gerar_dados
from graficos.plots import plot_mru


def main():
    t, s = gerar_dados(s0=0, v=10, tempo_final=10)
    plot_mru(t, s)


if __name__ == '__main__':
    main()