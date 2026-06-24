import matplotlib.pyplot as plt

def plot_linha(x, y, titulo='Gráfico', xlabel='x', ylabel='y'):
    plt.plot(x, y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_mru(t, s, salvar_caminho=None):
    plt.figure()
    plt.plot(t, s)
    plt.title("MRU - Movimento Retilíneo Uniforme")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid(True)
    if salvar_caminho:
        plt.savefig(salvar_caminho)
    plt.show()
    plt.close()


def plot_mruv(t, s, salvar_caminho=None):
    plt.figure()
    plt.plot(t, s)
    plt.title("MRUV - Movimento Retilíneo Uniformemente Variado")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid(True)
    if salvar_caminho:
        plt.savefig(salvar_caminho)
    plt.show()
    plt.close()
