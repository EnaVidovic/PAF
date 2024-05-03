import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from kosi_hitac import Projectile

if __name__ == "__main__":
    masa = 1.0  
    pocetna_brzina = 45.0  
    kut = 55  
    otpor_zraka = 0.2  
    dt = 0.1

    projektil = Projectile(masa, pocetna_brzina, kut, otpor_zraka, dt)
    #slučaj za Euler-ovu metodu
    projektil.simuliraj(5)  

    #slučaj za RK4 metodu
    projektil_rk4 = Projectile(masa, pocetna_brzina, kut, otpor_zraka, dt)
    projektil_rk4.simuliraj(5, koristi_rk4=True)  

    projektil.prikazi_graf()
    projektil_rk4.prikazi_graf(koristi_rk4=True)
    plt.show()

    