def get_data() -> list:
    with open('anagram.txt') as file:
        data = file.read().rstrip().split('\n')
    return data

DATA: list[str] = get_data()

ile_zrownowazonych: int = sum(d.count('0') == d.count('1') for d in DATA)
def ile_prawie_zrownowazonych() -> int:
    ile: int = 0
    for d in DATA:
        zera: int = d.count('0')
        jedynki: int = d.count('1')
        if (zera - jedynki == 1) or (jedynki - zera == 1):
            ile += 1
    return ile

with open('wynik.txt', 'a') as file:
    file.write('Zadanie 3.1\n')
    file.write(str(ile_zrownowazonych) + '\n')
    file.write(str(ile_prawie_zrownowazonych()) + '\n')

max_len = max(map(len, DATA))

anagramy = set()
def generuj_anagramy(ciag: list, index: int=0) -> set:
    #TODO: lepszy algorytm
    if index == len(ciag) - 1:
        anagramy.add(''.join(ciag))
    else:
        for i in range(index, len(ciag)):
            ciag[index], ciag[i] = ciag[i], ciag[index]
            generuj_anagramy(ciag, index + 1)
            ciag[index], ciag[i] = ciag[i], ciag[index]

ilosc = []
for d in DATA:
    if len(d) != max_len:
        pass
    generuj_anagramy()
    #TODO: nie wiem zrób coś