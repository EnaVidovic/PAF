import matplotlib.pyplot as plt

def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2
    
    if x1 == x2:
        return f"x = {x1}"
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        return f"y = {k}x + {n}"

def plot_pravac(tocka1, tocka2, graf_ime=None):
    x1, y1 = tocka1
    x2, y2 = tocka2

    plt.plot([x1, x2], [y1, y2], 'ro-', label="Točke")  
    plt.xlabel('x')
    plt.ylabel('y')
    
    pravac_jednadzba = jednadzba_pravca(tocka1, tocka2)
    plt.title(f"Pravac: {pravac_jednadzba}")

    plt.legend()
    
    if graf_ime is not None:
        plt.savefig(f"{graf_ime}.pdf")
        print(f"Graf spremljen kao '{graf_ime}.pdf'.")
    else:
        plt.show()

tocka1 = (2, 3)
tocka2 = (5, 7)

plot_pravac(tocka1, tocka2, "pravac_graf")