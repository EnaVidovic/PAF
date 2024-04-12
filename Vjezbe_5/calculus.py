import numpy as np

def derivacija_u_tocki(funkcija, tocka, epsilon=1e-6, metoda="trokorak"):
    
    if metoda == "trokorak":
        return (funkcija(tocka + epsilon) - funkcija(tocka - epsilon)) / (2 * epsilon)
    elif metoda == "dvokorak":
        return (funkcija(tocka + epsilon) - funkcija(tocka)) / epsilon
    else:
        raise ValueError("Nevažeća metoda. Molimo odaberite 'trokorak' ili 'dvokorak'.")

def derivacija_na_intervalu(funkcija, donja_granica, gornja_granica, epsilon=1e-6, metoda="trokorak"):
   
    tocke = np.linspace(donja_granica, gornja_granica, num=100)
    derivacije = [derivacija_u_tocki(funkcija, tocka, epsilon, metoda) for tocka in tocke]
    return tocke, derivacije


def pravokutna_aproksimacija(funkcija, donja_granica, gornja_granica, broj_podjela):
    
    dx = (gornja_granica - donja_granica) / broj_podjela
    x_vrijednosti = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)
    y_vrijednosti = funkcija(x_vrijednosti)
    donja_medja = dx * np.sum(y_vrijednosti[:-1])
    gornja_medja = dx * np.sum(y_vrijednosti[1:])
    return donja_medja, gornja_medja

def trapezna_formula(funkcija, donja_granica, gornja_granica, broj_podjela):
    
    dx = (gornja_granica - donja_granica) / broj_podjela
    x_vrijednosti = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)
    y_vrijednosti = funkcija(x_vrijednosti)
    integral = dx * (np.sum(y_vrijednosti) - 0.5 * (y_vrijednosti[0] + y_vrijednosti[-1]))
    return integral

