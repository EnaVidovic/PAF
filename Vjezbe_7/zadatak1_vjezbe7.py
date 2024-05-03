import matplotlib

matplotlib.use('TkAgg')
#kao i u prošlim vježnama prikazuje mi se problem sa backendom, pomoću ChatGPT-ja došla sam do ovog rješenja

import numpy as np
import matplotlib.pyplot as plt
from kosi_hitac import Projectile

if __name__ == "__main__":
    masa = 1.0  
    pocetna_brzina = 30.0  
    kut = 45  
    otpor_zraka = 0.1  
    dt_vrijednosti = [0.1, 0.05, 0.01, 0.005, 0.001]

    for dt in dt_vrijednosti:
        projektil = Projectile(masa, pocetna_brzina, kut, otpor_zraka, dt)
        projektil.simuliraj(5)  
        projektil.prikazi_graf()

#vrijednosti dt daju dovoljno precizno rješenje jer graf nema razlika u oscilacijama, te ide kontinuirano bez velikih oscilacija i oštrih 
#nagiba, da bi dobili ovako precizno rješenje potrebno je uzimati što manje vrijednosti dt-a, ukoliko rješenje nije precizno, smanjujemo
#vrijednosti i rješenje će biti bez oscilacija
#kao što ste naveli u prezentaciji Euler-ova metoda daje numerički stabilno rješenje samo za male vremenske intervale (dt vrijednosti)