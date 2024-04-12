import numpy as np
import matplotlib.pyplot as plt
from calculus import pravokutna_aproksimacija, trapezna_formula

def funkcija(x):
    return np.exp(-x**2)

analiticki_integral = np.sqrt(np.pi) / 2

donja_granica = 0
gornja_granica = 2

broj_koraka = [10, 50, 100, 200]

rezultati_pravokutna = []
rezultati_trapezna = []

for n in broj_koraka:
    donji_maks, gornji_maks = pravokutna_aproksimacija(funkcija, donja_granica, gornja_granica, n)
    rezultati_pravokutna.append((donji_maks, gornji_maks))
    
    integral_trapezna = trapezna_formula(funkcija, donja_granica, gornja_granica, n)
    rezultati_trapezna.append(integral_trapezna)


plt.figure(figsize=(10, 6))
plt.axhline(y=analiticki_integral, color='r', linestyle='--', label='Analitičko rješenje')


donje_maks = [donja for donja, _ in rezultati_pravokutna]
gornje_maks = [gornja for _, gornja in rezultati_pravokutna]
plt.plot(broj_koraka, donje_maks, label='Pravokutna (donji maks)')
plt.plot(broj_koraka, gornje_maks, label='Pravokutna (gornji maks)', linestyle='--')


plt.plot(broj_koraka, rezultati_trapezna, label='Trapezna formula', linestyle='-.')
plt.xlabel('Broj koraka')
plt.ylabel('Vrijednost integrala')
plt.title('Numerička integracija funkcije $e^{-x^2}$')
plt.legend()
plt.grid(True)
plt.show()