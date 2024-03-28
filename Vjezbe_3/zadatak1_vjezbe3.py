#(a)

a = 5.0
b = 4.935
ocekivani_rezultat = 0.065
python = a - b

print("(a)\n", python)

#Ovo se događa zbog načina na koji računalni sustavi prepoznaju i spremaju decimalne brojeve s pomičnim zarezom. 
#Budući da računalni sustavi koriste binarni sustav za pohranu brojeva, 
#neki decimalni brojevi imaju netočan zapis u binarnom sustavu, što može pokazati male
#greške u točnosti pri računanju.

#(b)

x = 0.1
y = 0.2
z = 0.3

uk = x + y + z

print("(b)\n",uk)

#Ovo se događa zbog nepravilnosti u pohrani decimalnih brojeva u računalima. 
#Brojevi poput 0.1, 0.2 i 0.3 nemaju točan binarni ekvivalent koji se može spremiti u računalu, pa se prilikom izvođenja aritmetičkih operacija može doći  grešaka u točnosti.
#Iako bismo očekivali da je rezultat 0.6, zbog nepravilnosti pohrane decimalnih brojeva u računalima, Python vraća 0.6000000000000001.