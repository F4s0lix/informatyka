# stworzono przez github.com/F4s0lix

from itertools import permutations

def get_data() -> list:
    """
    funkcja zwraca listę danych z pliku, każda komórka to kolejna linia pliku 
    """
    with open('anagram.txt') as file: # otwieranie pliku
        data = file.read().rstrip().split('\n') # czytanie, usuwanie białych znaków, rozdzielenie 
    return data

DATA: list[str] = get_data() # stała z wartościami z pliku

# suma liczb binarnych, w których liczba 0 jest równa liczbie 1 
ile_zrownowazonych: int = sum(d.count('0') == d.count('1') for d in DATA)
# suma liczb binarnych, w których bezwzględnia różncia ilości 0 i 1 jest równa 1
ile_prawie_zrownowazonych: int = sum(abs(d.count('1') - d.count('0')) == 1 for d in DATA)

with open('wynik.txt', 'a') as file: # otwórz plik w trybie dopisywania
    file.write('Zadanie 3.1\n') #zapisywanie odpowiedzi
    file.write(str(ile_zrownowazonych) + '\n')
    file.write(str(ile_prawie_zrownowazonych) + '\n')


permutacje_wszystkich: list[list[str]] = [] # zmienna pomocnicza zawierające listę list z permutacjami
for d in DATA: # dla każdej wartości z DATA
    if len(d) != 8: # jeżeli długość liczby binarnej jest różna od 8
        permutacje_wszystkich.append(False) # nie liczymy, ponieważ zadanie tego nie wymaga
    else:
        perm: list = list(set(''.join(i) for i in permutations(d))) # lista UNIKALNYCH anagramów jakie można zrobić z liczby
        permutacje_wszystkich.append(perm) # dodaje permutacje do listy z wszystkimi dla każdej wartości z DATA 

for i in range(len(permutacje_wszystkich)): # dla i w zasięgu długości listy
    if permutacje_wszystkich[i]: # jeżeli nie jest False
        permutacje_wszystkich[i] = [x for x in permutacje_wszystkich[i] if not x.startswith('0')] # dodaje wszystkie wartości oprócz tych, które zaczynają się od 0

ilosc_anagramow: list = list(map(lambda x: len(x) if x else False, permutacje_wszystkich)) # liczy długość listy, jeżeli wartość jest listą
najwiecej: int = max(ilosc_anagramow) # największa ilość anagramów
wynik: list = [DATA[i] for i in range(len(DATA)) if ilosc_anagramow[i] == najwiecej] # tworzy listę z liczbą, z której powstały anagramy jeżeli ilość jej anagramów jest równa największej

with open('wynik.txt', 'a') as file: # zapisywanie odpowiedzi 
    file.write('\nZadanie 3.2\n')
    for w in wynik:
        file.write(w + '\n')

# lista z absolutną różnicą sąsiadujących liczb
bezwzgledna_roznica: list = [abs(int(DATA[i], 2) - int(DATA[i + 1], 2)) for i in range(len(DATA) - 1)] # najpier przekonwertujemy binarne na dziesiętne, potem odejmujemy je, ustawiamy jako liczba bezwzględna dla wszystkich wartości w DATA 
najwieksza: int = max(bezwzgledna_roznica) # największa różnica
with open('wynik.txt', 'a') as file:
    file.write('\nZadanie 3.3\n')
    file.write(bin(najwieksza)[2:] + '\n') # zmieniamy na binarne i pozbywamy się prefixu

DATAdzies: list[int] = [int(i, 2) for i in DATA] # zmieniamy wszystkie liczby binarne z DATA na dziesiętne

a: int = sum(str(d).count('0') == 0 for d in DATAdzies) # ilość liczb bez cyfry 0
b: list = [sum(set(int(c) for c in str(d))) for d in DATAdzies] # suma unikalnych cyfr w każdej liczbie z DATAdzies

with open('wynik.txt', 'a') as file: # zapisywanie odpowiedzi
    file.write('\nZadanie 3.4\n')
    file.write(str(a) + '\n')
    file.write(str(DATAdzies[b.index(max(b))])) # liczba z największą sumą unikalnych cyfr
    # wypisuje wartość z DATAdzies o indeksie, w którym suma unikalnych cyfr jest największa