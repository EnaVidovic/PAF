import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11
Ms = 1.989e30
Mz = 5.9742e24
AU = 1.486e11
v_okomita = 29783
dana_u_godini = 365.242

def ubrzanje(r_sunce, r_zemlja):
    udaljenost = r_zemlja - r_sunce
    F_gravitacija = -G * Ms * Mz / np.linalg.norm(udaljenost)**3 * udaljenost
    akceleracija_zemlje = F_gravitacija / Mz
    return akceleracija_zemlje

t_pocetak = 0
t_kraj = dana_u_godini * 1
dt = 1

r_sunce = np.array([0, 0])
r_zemlja = np.array([AU, 0], dtype=float)
v_zemlja = np.array([0.0, v_okomita], dtype=float)

theta = np.linspace(0, 2*np.pi, 1000)
x_elipsa = AU * np.cos(theta)
y_elipsa = AU * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x_elipsa, y_elipsa, label='Zemlja')
plt.plot(0, 0, 'ro', label='Sunce')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Zemlje oko Sunca')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#dovivamo sunce koje je u položaju 0,0 i oko njega  simuliranu putanju zemlje








