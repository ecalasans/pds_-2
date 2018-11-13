import numpy as np
import matplotlib.pyplot as plt

DOIS_PI = 2 * np.pi
PI = 'π'

def DFT(x_n, N=0):
    '''
    Função que calcula a DFT para uma determinada sequência

    :param x_n: sequência x[n]
    :param N: número de pontos desejados para a DFT
    :return: array com os valores da DFT para x[n]
    '''

    # Cálculo da definição da frequência(Omega0)
    Omega0 = DOIS_PI / (N)

    # Inicializa x[k]
    x_k = np.zeros(N, dtype=np.complex_)

    # Cálculo de x[k]
    for k in range(N):
        soma = 0
        for n in range(len(x_n)):
            expComplexa = np.exp(-1j * Omega0 * k * n)
            produto = x_n[n] * expComplexa
            soma = soma + produto
        x_k[k] = soma

    return (x_k, Omega0)

x = np.random.randint(1, 3, 4)

# Cálculo de x1_[k]
x1_k = DFT(x, 100)

k = np.arange(len(x1_k[0]))

kOmega0 = k * x1_k[1]
locs = np.linspace(0, len(k), 5)
labels_x = []

print(locs)
plt.stem(kOmega0, np.abs(x1_k[0]), '-')
plt.xticks(np.linspace(0,6,5), tuple(labels_x))
plt.subplots_adjust(right=3, top=2)
plt.show()