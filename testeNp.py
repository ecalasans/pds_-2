import numpy as np
import matplotlib.pyplot as plt
import cmath

DOIS_PI = 2 * np.pi
PI = 'π'

def DFT(N=0, freqs=[]):
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

    k = np.arange(0, N)

    # Cálculo de x[k]
    somaFreq = 0
    for f in freqs:
        omega = DOIS_PI * f
        fator1 = omega - k*Omega0
        fator2 = omega + k*Omega0
        frac1 = ((1 - np.exp(1j * N * fator1))/(1 - np.exp(1j * fator1)))
        frac2 = ((1 - np.exp(-1j * N * fator2))/(1 - np.exp(-1j * fator2)))

        somaFreq = somaFreq + ((1/2j) *(frac1 - frac2))

        x_k = somaFreq

    return (x_k, Omega0)

frequencias = [5, 53, 539]

# Cálculo de x1_[k]
x1_k = DFT(30000, frequencias)

print()
