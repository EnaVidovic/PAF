def unos_tocke():
    while True:
        try:
            x = float(input("Upišite x koordinatu: "))
            y = float(input("Upišite y koordinatu: "))
            return x, y
        except ValueError:
            print("Neispravan unos. Molimo pokušajte ponovno.")

def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2
    
    if x1 == x2:
        return f"x = {x1}"
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        return f"y = {k}x + {n}"

def main():
    print("Unesite koordinate prve točke:")
    tocka1 = unos_tocke()
    print("Unesite koordinate druge točke:")
    tocka2 = unos_tocke()
    
    print("Jednadžba pravca koji prolazi kroz te dvije točke je:")
    print(jednadzba_pravca(tocka1, tocka2))

if __name__ == "__main__":
    main()