import numpy as np
import matplotlib.pyplot as plt

class NabijenaČestica:
    def __init__(self, masa, naboj, početno_stanje, električno_polje, magnetsko_polje, dt):
        self.masa = masa
        self.naboj = naboj
        self.stanje = np.array(početno_stanje)
        self.E = električno_polje
        self.B = magnetsko_polje
        self.dt = dt
        self.x=[0]
        self.y=[0]
        self.z=[0]

    def lorentzova_sila(self, E, B):
        F = self.naboj * (E + np.cross(self.stanje[3:], B))
        return F

    def kretanje(self, E, B, dt):
        a = self.lorentzova_sila(E, B) / self.masa 
        self.stanje[3:] += a * dt
        self.x.append(self.stanje[3] * dt + self.x[-1])
        self.y.append(self.stanje[4] * dt + self.y[-1])
        self.z.append(self.stanje[5] * dt + self.z[-1])

    def simuliraj(self, trajanje):
        for _ in np.arange(0, trajanje, self.dt):
            self.kretanje(self.E, self.B, self.dt)

    def prikaži_putanju(self, naslov):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        putanja = [self.x, self.y, self.z]
        ax.plot(putanja[0], putanja[1], putanja[2])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(naslov)
        plt.show()