import numpy as np
import matplotlib.pyplot as plt


import matplotlib
matplotlib.use('Agg')

class HarmonicOscillator:
    def __init__(self, masa, elasticna_konstanta, pocetni_polozaj, pocetna_brzina):
        self.masa = masa
        self.elasticna_konstanta = elasticna_konstanta
        self.polozaj = pocetni_polozaj
        self.brzina = pocetna_brzina
    
    def azuriraj(self, dt):
        ubrzanje = -self.elasticna_konstanta / self.masa * self.polozaj
        self.brzina += ubrzanje * dt
        self.polozaj += self.brzina * dt
    
    def rjesi(self, dt, ukupno_vrijeme):
        broj_koraka = int(ukupno_vrijeme / dt)
        polozaji = np.zeros(broj_koraka)
        brzine = np.zeros(broj_koraka)
        ubrzanja = np.zeros(broj_koraka)
        vremena = np.linspace(0, ukupno_vrijeme, broj_koraka)

        for i in range(broj_koraka):
            polozaji[i] = self.polozaj
            brzine[i] = self.brzina
            ubrzanja[i] = -self.elasticna_konstanta / self.masa * self.polozaj
            self.azuriraj(dt)

        return vremena, polozaji, brzine, ubrzanja
    
    
    def period_titranja(self, dt, tolerance=1e-6, max_iter=1000000000):
        pocetni_polozaj = self.polozaj
        t = 0
        
        while True:
            self.azuriraj(dt)
            t += dt
            
            #služi nam za provjeru je li osciliranje periodično
            if abs(self.polozaj - pocetni_polozaj) < tolerance:
                break
                
            if t > max_iter * dt:
                raise ValueError("Maksimalni broj iteracija premašen. Oscilacija možda nije periodična.")
        
        return 2 * t

