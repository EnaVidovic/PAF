import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator 

#iz nekog razloga prilikom upisivanja koda u terminalu mi se pojavljivala greska u vezi 'Backenda' te sam pomocu ChatGPT-ja 
#i raznih priručnika s Google-a došla do zaključka da sam morala postaviti 'interactive backend' te se nadam da to neće utjecati na 
#ostatak zadatka

import matplotlib
matplotlib.use('Agg')


masa = 1.0  
elasticna_konstanta = 1.0 
pocetni_polozaj = 1.0  
pocetna_brzina = 0.0  

oscilator = HarmonicOscillator(masa, elasticna_konstanta, pocetni_polozaj, pocetna_brzina)

dt_vrijednosti = [0.1, 0.05, 0.01]  
ukupno_vrijeme = 10.0  # s


for dt in dt_vrijednosti:
    vremena, polozaji, brzine, ubrzanja = oscilator.rjesi(dt, ukupno_vrijeme)

    plt.figure(figsize=(12, 4))

    #crtanje x-t grafa
    plt.subplot(1, 3, 1)
    plt.plot(vremena, polozaji)
    plt.title("x - t graf")
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Položaj (m)")

    #crtanje v-t grafa
    plt.subplot(1, 3, 2)
    plt.plot(vremena, brzine)
    plt.title("v - t graf")
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Brzina (m/s)")

    #crtanje a-t graga
    plt.subplot(1, 3, 3)
    plt.plot(vremena, ubrzanja)
    plt.title("a - t graf")
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Ubrzanje (m/s^2)")

    plt.tight_layout()

    plt.savefig(f"graf_dt_zadatak1_{dt}.png")

    
