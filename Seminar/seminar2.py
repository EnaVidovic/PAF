import numpy as np
import matplotlib.pyplot as plt

def provjeri_polozaj_tocke(x_tocke, y_tocke, x_centra, y_centra, radijus, spremi=False, ime_slike=None):
    udaljenost = np.sqrt((x_tocke - x_centra)**2 + (y_tocke - y_centra)**2)

    if udaljenost < radijus:
        polozaj = 'unutar'
    elif udaljenost == radijus:
        polozaj = 'na'
    else:
        polozaj = 'izvan'

    fig, ax = plt.subplots()
    ax.add_patch(plt.Circle((x_centra, y_centra), radijus, color = 'c', fill = False))

    plt.plot(x_tocke, y_tocke, 'ro', label = 'Točka')
    plt.xlabel('X-os')
    plt.ylabel('Y-os')
    plt.title('Položaj točke u odnosu na kružnicu')
    plt.axis('equal')
    plt.legend()

    print(f"Točka se nalazi {polozaj} kružnice. Udaljena je za {udaljenost: .2f}.")

    if spremi:
        if ime_slike is None:
           ime_slike = 'polozaj_tocke.png'
        plt.savefig(ime_slike)
        print(f"Slika spremljena kao '{ime_slike}'.")

    plt.show()

provjeri_polozaj_tocke(1,0,1,1,1, True, "tocnona.png")



    