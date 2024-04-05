import numpy as np
import matplotlib.pyplot as plt

v0 = 10  
theta = 60  
x0 = 0  
y0 = 0 
duration = 10  
analiticki_domet = (v0 ** 2) * np.sin(2 * np.radians(theta)) / 9.81  

#postavljanje više različitih vrijednosti za dt
dt_values = np.linspace(0.001, 0.1, 100)

#ponovno uspoređujemo analitički i numerički način te računamo relativnu pogrešku
relativna_pogreska = []
for dt in dt_values:
    particle = (v0, theta, x0, y0)
    numericki_domet = particle.range(dt)
    relativna_pogreska.append(abs(numericki_domet - analiticki_domet) / analiticki_domet)


plt.plot(dt_values, relativna_pogreska)
plt.title('Ovisnost relativne pogreške o vremenskom koraku')
plt.xlabel('Vremenski korak (dt)')
plt.ylabel('Relativna pogreška')
plt.xscale('log')  
plt.yscale('log')
plt.grid(True)
plt.show()

#iako sam definirala klasu particle, program mi konstantno izbacuje da particle nije definiran, 
#uz pomoć Google-a i ChatGP-a pokušala sam riješiti problem, ali unatoč svemu program se i dalje ne želi pokrenuti
