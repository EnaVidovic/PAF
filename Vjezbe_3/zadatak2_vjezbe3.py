def izračunaj_rezultat(N):
    rezultat = 0
    for _ in range(N):
        rezultat += 1/3
    for _ in range(N):
        rezultat -= 1/3
    rezultat -= 5
    return rezultat

iteracije = [200, 2000, 20000]
for iteracija in iteracije:
    konačni_rezultat = izračunaj_rezultat(iteracija)
    print("Broj iteracija:", iteracija,", Konačni rezultat:", konačni_rezultat)

#Konačni rezulztati su oko 0, ali zbog nesavršenosti u radu s brojevima s pomičnim zarezom, rezultati imaju manja odstupanja.