from itertools import permutations
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

permutacje_wszystkich: list[list[str]] = []
for d in DATA:
    if len(d) != 8:
        permutacje_wszystkich.append(None)
    else:
        perm = list(set(''.join(i) for i in permutations(d)))
        permutacje_wszystkich.append(perm)

for l in permutacje_wszystkich:
    if l is not None:
        for a in l:
            if a.startswith('0'):
                l.remove(a)

    
najwiecej = max(map(lambda x: len(x) if x is not None else 0, permutacje_wszystkich))
print(najwiecej) #FIXME: XDD CO TO JEST
#jeżeli wypisze się max(map...) to wypisuje 48. Jeżeli przypisze się do zmiennej i wypisze to wyjdzie 47. Obie odpowiedzi są złe xdd

bezwzgledna_roznica = [abs(int(DATA[i], 2) - int(DATA[i + 1], 2)) for i in range(len(DATA) - 1)]
najwieksza = max(bezwzgledna_roznica)
with open('wynik.txt', 'a') as file:
    file.write('Zadanie 3\n')
    file.write(bin(najwieksza)[2:] + '\n')

DATAdzies = [int(i, 2) for i in DATA]

a = sum(str(d).count('0') == 0 for d in DATAdzies)
b = [sum(set(int(c) for c in str(d))) for d in DATAdzies]
with open('wynik.txt', 'a') as file:
    file.write('Zadanie 3.4\n')
    file.write(str(a) + '\n')
    file.write(str(DATAdzies[b.index(max(b))]))