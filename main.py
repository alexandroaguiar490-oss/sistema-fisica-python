from simulacoes.mru import gerar_dados
from simulacoes.mruv import gerar_dados_mruv
from graficos.plots import plot_mru, plot_mruv


def main():
    t, s = gerar_dados(s0=0, v=10, tempo_final=10)
    plot_mru(t, s, salvar_caminho="assets/mru_grafico.png")

    t_mruv, s_mruv = gerar_dados_mruv(velocidade_inicial=0, aceleracao=2, tempo_final=10)
    plot_mruv(t_mruv, s_mruv, salvar_caminho="assets/mruv_grafico.png")


if __name__ == '__main__':
    main()