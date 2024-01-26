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
        permutacje_wszystkich.append(False)
    else:
        perm = list(set(''.join(i) for i in permutations(d)))
        permutacje_wszystkich.append(perm)

for l in permutacje_wszystkich:
    if l:
        for a in l:
            if a.startswith('0'):
                l.remove(a)

    
for i in range(len(permutacje_wszystkich)):
    if permutacje_wszystkich[i]:
        permutacje_wszystkich[i] = [x for x in permutacje_wszystkich[i] if not x.startswith('0')] #działa
ilosc_anagramow = list(map(lambda x: len(x) if x else False, permutacje_wszystkich))
najwiecej = max(ilosc_anagramow)
wynik = [DATA[i] for i in range(len(DATA)) if ilosc_anagramow[i] == najwiecej]

with open('wynik.txt', 'a') as file:
    file.write('\nZadanie 3.2\n')
    for w in wynik:
        file.write(w + '\n')

bezwzgledna_roznica = [abs(int(DATA[i], 2) - int(DATA[i + 1], 2)) for i in range(len(DATA) - 1)]
najwieksza = max(bezwzgledna_roznica)
with open('wynik.txt', 'a') as file:
    file.write('\nZadanie 3.3\n')
    file.write(bin(najwieksza)[2:] + '\n')

DATAdzies = [int(i, 2) for i in DATA]

a = sum(str(d).count('0') == 0 for d in DATAdzies)
b = [sum(set(int(c) for c in str(d))) for d in DATAdzies]
with open('wynik.txt', 'a') as file:
    file.write('\nZadanie 3.4\n')
    file.write(str(a) + '\n')
    file.write(str(DATAdzies[b.index(max(b))]))