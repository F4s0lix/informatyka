def wczytaj_dane():
    with open('Dane_PR2/pary.txt') as file:
        dane_wierszami = file.read().strip().split('\n')
        dane_parami = [d.split(' ') for d in dane_wierszami]
        return dane_parami

DANE = wczytaj_dane()

def is_prime(n):
    return n > 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def zadanie_pierwsze(n):
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n - i):
            return [i, n - i]
    return False

print('ZADANIE 1')
for liczba, _ in DANE:
    goldbach = zadanie_pierwsze(int(liczba))
    if goldbach:
        a, b = goldbach
        print(liczba, a, b)

def zadanie_drugie():
    dane_zadania = [d[1] for d in DANE] # tylko slowa
    for slowo in dane_zadania:
        wynik = {litera: slowo.count(litera) for litera in set(slowo)}
        najwiecej_powtorzen = {d: wynik[d] for d in wynik.keys() if wynik[d] == max(wynik.values())}
        for key, value in najwiecej_powtorzen.items():
            print(key * value, value)

print('ZADANIE 2')
zadanie_drugie()
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx')

def zadanie_trzecie():
    ta_sama_dlugosc = [[liczba, slowo] for liczba, slowo in DANE if int(liczba) == len(slowo)]
    liczby = [i[0] for i in ta_sama_dlugosc]
    slowa = [i[1] for i in ta_sama_dlugosc]
    print(min(liczby), min(slowa))
print('ZADANIE 3')
zadanie_trzecie()