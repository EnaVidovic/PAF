import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = np.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)
        self.t = 0

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= 9.81 * dt  # Gravitacijsko ubrzanje

    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt=0.01):
        self.reset()
        x_values = [self.x]
        y_values = [self.y]
        while self.y >= 0:
            self.__move(dt)
            x_values.append(self.x)
            y_values.append(self.y)
        plt.plot(x_values, y_values)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Putanja čestice u x-y ravnini')
        plt.grid(True)
        plt.show()



v0 = 10  
theta = 45  
x0 = 0  
y0 = 0  

#postavljamo objekt čestice
particle = Particle(v0, theta, x0, y0)

#budući da trebamo usporediti rezultate dobivene numerički i analitički, računamo na oba načina

numericki_domet = particle.range()
print("Numerički izračunati domet:", numericki_domet, "m")

analiticki_domet = (v0 ** 2) * np.sin(2 * np.radians(theta)) / 9.81
print("Analitički izračunati domet:", analiticki_domet, "m")

#izračunat ćemo i odstupanje dva ponuđena rezultata
odstupanje = abs(numericki_domet - analiticki_domet)
print("Odstupanje između numeričkog i analitičkog dometa:", odstupanje, "m")

particle.plot_trajectory()


