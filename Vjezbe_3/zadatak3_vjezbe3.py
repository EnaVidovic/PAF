#a)

def aritmeticka_sredina(lista):
    return sum(lista)/len(lista)

def standardna_devijacija(lista):
    aritmeticka = aritmeticka_sredina(lista)
    devijacija = sum((x - aritmeticka) ** 2 for x in lista) / len(lista)
    return devijacija ** 0.5

def main():
    tocke = [4, 7, 18, 20, 22, 26, 28, 30, 31, 35]

    print("Aritmetička sredina a):", aritmeticka_sredina(tocke))
    print("Standardna devijacija a):", standardna_devijacija(tocke))

if __name__ == "__main__":
    main()

#b
import numpy as np
import statistics

def main():
    tocke = [4, 7, 18, 20, 22, 26, 28, 30, 31, 35]

    print("Aritmetička sredina b):", np.mean(tocke))
    print("Standardna devijacija b):", np.std(tocke))

if __name__ == "__main__":
    main()