import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator 

if __name__ == "__main__":
    masa = 1.0 
    elasticna_konstanta = 1.0  
    pocetni_polozaj = 1.0  
    pocetna_brzina = 0.0  

    oscilator = HarmonicOscillator(masa, elasticna_konstanta, pocetni_polozaj, pocetna_brzina)

    dt_vrijednosti = [0.1, 0.05, 0.01, 0.005, 0.001] 

    for dt in dt_vrijednosti:
        period = oscilator.period_titranja(dt)
        print(f"Period titranja za dt={dt}: {period} s")

#prilikom prvog rješavanja zadatka pojavio se ValueError kao što sam i postavila u kodu, gdje je bio premašen max. broj iteracija,
#nakon čega sam povećala broj iteracija te dobila rezultate
#promjene perioda smanjuju se smanjenjem odabranog dt