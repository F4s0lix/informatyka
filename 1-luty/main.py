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

permutacje_wszystkich: list[int] = []
for d in DATA:
    if len(d) != 8:
        permutacje_wszystkich.append(False)
    else:
        perm = permutations(d)
        temp = []
        for p in perm:
            anagram = ''.join(p)
            if not anagram.startswith('0'):
                temp.append(anagram)
        permutacje_wszystkich.append(temp)
    #FIXME: nie usuwa powtórzeń chyba
print([len(i) for i in permutacje_wszystkich if i])
#najwiecej = max(permutacje_wszystkich)
#anagramy = [DATA[i] for i in range(len(DATA)) if permutacje_wszystkich[i] == najwiecej]
#with open('wynik.txt', 'a') as file:
#    file.write('Zadanie 3.2\n')
#    for a in anagramy:
#        file.write(a + '\n') #FIXME: coś nadal nie działa

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