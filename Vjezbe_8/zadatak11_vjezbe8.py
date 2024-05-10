
import numpy as np
import matplotlib.pyplot as plt
from polja import NabijenaČestica


masa_e = 1 
masa_p = masa_e 
q_e = -1 
q_p = -q_e  


početno_stanje_e = [0, 0, 0, 0.1, 0.1, 0.1]  
početno_stanje_p = [0, 0, 0, 0.1, 0.1, 0.1]  
E = np.array([0, 0, 0])  
B = np.array([0, 0, 1])  

elektron = NabijenaČestica(masa_e, q_e, početno_stanje_e, E, B, dt=0.01)
pozitron = NabijenaČestica(masa_p, q_p, početno_stanje_p, E, B, dt=0.01)


 

elektron.simuliraj(10)  
#sim_p.simuliraj(10)  

elektron.prikaži_putanju("Putanja elektrona")
#sim_p.prikaži_putanju("Putanja pozitrona")

pozitron.simuliraj(10)

pozitron.prikaži_putanju("Putanja pozitrona")


#elektron se giba u suprotnom smjeru u odnosu na smjer pozitivnog električnog polja i smjer negativne električne struje
#pozitron se giba u smjeru pozitivnog električnog polja i u smjeru negativne električne struje
#u kodu oni imaju istu masu, a suprotne naboje naboje, što znači da će im putanje kretanja biti suprotne