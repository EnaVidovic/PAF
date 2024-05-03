import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt



class Projectile:
    def __init__(self, masa, pocetna_brzina, kut, otpor_zraka, dt):
        self.masa = masa
        self.pocetna_brzina = pocetna_brzina
        self.kut = np.radians(kut) 
        self.otpor_zraka = otpor_zraka
        self.dt = dt
        
        self.vx = self.pocetna_brzina * np.cos(self.kut)
        self.vy = self.pocetna_brzina * np.sin(self.kut)
        
        self.x = [0.0]
        self.y = [0.0]

    def azuriraj(self):
        ax = -(self.otpor_zraka / self.masa) * self.vx
        ay = -(self.otpor_zraka / self.masa) * self.vy - 9.81 
        #ovim računamo ubrzanje uz otpor zraka
        
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        
        self.x.append(self.x[-1] + self.vx * self.dt)
        self.y.append(self.y[-1] + self.vy * self.dt)
        #računanje položaja u i x i y smjeru

#dodajemo Range-Kutta metodu 4. reda
    def azuriraj_rk4(self):
        k1vx = -(self.otpor_zraka / self.masa) * self.vx
        k1vy = -(self.otpor_zraka / self.masa) * self.vy - 9.81
        
        k2vx = -(self.otpor_zraka / self.masa) * (self.vx + 0.5 * k1vx * self.dt)
        k2vy = -(self.otpor_zraka / self.masa) * (self.vy + 0.5 * k1vy * self.dt) - 9.81
        
        k3vx = -(self.otpor_zraka / self.masa) * (self.vx + 0.5 * k2vx * self.dt)
        k3vy = -(self.otpor_zraka / self.masa) * (self.vy + 0.5 * k2vy * self.dt) - 9.81
        
        k4vx = -(self.otpor_zraka / self.masa) * (self.vx + k3vx * self.dt)
        k4vy = -(self.otpor_zraka / self.masa) * (self.vy + k3vy * self.dt) - 9.81
        
        self.vx += (k1vx + 2 * k2vx + 2 * k3vx + k4vx) * self.dt / 6
        self.vy += (k1vy + 2 * k2vy + 2 * k3vy + k4vy) * self.dt / 6
        
        self.x.append(self.x[-1] + self.vx * self.dt)
        self.y.append(self.y[-1] + self.vy * self.dt)

    def simuliraj(self, vrijeme, koristi_rk4=False):
        broj_koraka = int(vrijeme / self.dt)
        for _ in range(broj_koraka):
            if koristi_rk4:
                self.azuriraj_rk4()
            else:
                self.azuriraj()

    def prikazi_graf(self, koristi_rk4=False):
       if not koristi_rk4:
            plt.plot(self.x, self.y, label='Euler')
       else:
            plt.plot(self.x, self.y, label='RK4')
       plt.xlabel('x (m)')
       plt.ylabel('y (m)')
       plt.title('Kosi hitac s otporom zraka')
       plt.grid(True)
       plt.legend()