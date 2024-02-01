from math import sqrt

def sito(n: int) -> list:
    czy_pierwsza = [True] * (n + 1)
    
    for num in range(2, int(n**0.5) + 1):
        if czy_pierwsza[num]:
            for multiple in range(num * num, n + 1, num):
                czy_pierwsza[multiple] = False

    return [i for i in range(len(czy_pierwsza)) if czy_pierwsza[i]]

with open('liczby.txt') as plik:
    liczby: list = [int(liczba) for liczba in plik.read().rstrip().split('\n')]

liczby_pierwsze: tuple = tuple(sito(max(liczby)))

ile_to_pierwsze: int = sum(num - 1 in liczby_pierwsze for num in liczby)
with open('wyniki3.txt', 'a') as plik:
    plik.write('Zadanie 3.2\n' + f'{ile_to_pierwsze}\n')


def pierwsza(n: int) -> bool:
    if n < 2:
        return False

    range_limit = int(sqrt(n)) + 1

    for i in range(2, range_limit):
        if n % i == 0:
            return False
    return True

liczby_parzyste = list(filter(lambda x: x % 2 == 0, set(liczby)))
najwieksza = [0, 0] # [liczba, powtorzenia]
najmniejsza = [0, max(liczby_parzyste)] # j.w.
for liczba in liczby_parzyste:
    powt = 0
    for i in range(2, liczba // 2 + 1):
        if pierwsza(i) and pierwsza(liczba - i):
            powt += 1
    if najwieksza[1] < powt:
        najwieksza = [liczba, powt]
    if najmniejsza[1] > powt:
        najmniejsza = [liczba, powt]

with open('wyniki3.txt', 'a') as plik:
    plik.write(f'Zadanie 3.3\n {najwieksza[0]} {najwieksza[1]} {najmniejsza[0]} {najmniejsza[1]}\n')

HEX_CYFRY: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
liczby_hex: str = ''.join(map(lambda x: hex(x)[2:], liczby)).upper()

hex_ilosc: dict = {key: liczby_hex.count(key) for key in HEX_CYFRY}
with open('wyniki3.txt', 'a') as plik:
    plik.write('Zadanie 3.4\n')
    for key, value in hex_ilosc.items():
        plik.write(f'{key}:{value}\n')

