from string import ascii_uppercase

def zadanie_pierwsze(wejscie: list) -> int:
    wynik = 0
    for i in wejscie:
        krok = i.split(' ')[0]
        if krok == 'DOPISZ': wynik += 1
        if krok == 'USUN': wynik -= 1
    return wynik

def zadanie_drugie(wejscie: list) -> list:
    najlepsze = ['Start', 0]
    poprzedni = 'Start'
    dlugosc = 0
    for index, item in enumerate(wejscie):
        krok = item.split(' ')[0]
        if krok == poprzedni:
            dlugosc += 1
        else:
            if dlugosc > najlepsze[1]: najlepsze = [wejscie[index - 1].split(' ')[0], dlugosc]
            poprzedni = krok
            dlugosc = 1
    return najlepsze

def zadanie_trzecie(wejscie: list) -> tuple:
    litery = {}
    for i in wejscie:
        krok = i.split(' ')
        if krok[0] == 'DOPISZ':
            if krok[1] in litery.keys():
                litery[krok[1]] += 1
            else:
                litery[krok[1]] = 1
    wynik = max(litery)
    return wynik, litery[wynik]

def zadanie_czwarte(wejscie: list) -> str:
    slowo = []
    alfabet = ascii_uppercase
    for i in wejscie:
        krok = i.split(' ')
        if krok[0] == 'DOPISZ': slowo.append(krok[1])
        if krok[0] == 'USUN': slowo.pop()
        if krok[0] == 'ZMIEN': slowo[-1] = krok[1]
        if krok[0] == 'PRZESUN':
            index = slowo.index(krok[1])
            if krok[1] == 'Z': slowo[index] = 'A'
            else: slowo[index] = alfabet[alfabet.index(slowo[index]) + 1]
    return ''.join(slowo)

dane = [w.strip() for w in open('DANE_2105/instrukcje.txt').read().split('\n')]
print(dane[0])
print('=' * 30)
print('ZADANIE 4.1')
print(zadanie_pierwsze(dane))
print('=' * 30)
print('ZADANIE 4.2')
print(zadanie_drugie(dane))
print('=' *30)
print('ZADANIE 4.3')
print(zadanie_trzecie(dane))
print('=' * 30)
print('ZADANIE 4.4')
print(zadanie_czwarte(dane))