import numpy as np
import matplotlib.pyplot as plt

from calculus import derivacija_u_tocki, derivacija_na_intervalu


def trigonometrijska_funkcija(x):
    return np.sin(x)

def kubna_funkcija(x):
    return x ** 3

donja_granica = -2
gornja_granica = 2

tocke_trig, derivacije_trig = derivacija_na_intervalu(trigonometrijska_funkcija, donja_granica, gornja_granica)

tocke_kubna, derivacije_kubna = derivacija_na_intervalu(kubna_funkcija, donja_granica, gornja_granica)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tocke_trig, trigonometrijska_funkcija(tocke_trig), label='sin(x)', color='blue')
plt.plot(tocke_trig, derivacije_trig, label='Derivacija sin(x)', linestyle='--', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometrijska funkcija i njena derivacija')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(tocke_kubna, kubna_funkcija(tocke_kubna), label='x^3', color='green')
plt.plot(tocke_kubna, derivacije_kubna, label='Derivacija x^3', linestyle='--', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kubna funkcija i njena derivacija')
plt.legend()

plt.tight_layout()
plt.show()

