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

najwiecej_anagramow = [d for d in DATA if d.count('0') == d.count('1')]
#FIXME: BŁĄD - jeżeli są większe można zrobić więcej anagramów
with open('wynik.txt', 'a') as file:
    file.write('Zadanie 3.2\n')
    for a in najwiecej_anagramow:
        file.write(a + '\n')