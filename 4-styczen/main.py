def get_data() -> list:
    with open('temperatury_nowy_york.txt') as file:
        file: list = file.read().split('\n')
    data: list = []
    for date in file:
        data.append(date.split(' '))
    for date in data:
        date[1] = int(date[1])
    return data

DATA: list = get_data()
NAZWA_DNI: dict = {
    0: 'piątek',
    1: 'sobota',
    2: 'niedziela',
    3: 'poniedziałek',
    4: 'wtorek',
    5: 'środa',
    6: 'czwartek',
}

def oblicz_srednia(data) -> float:
    suma: int = 0
    for date in data:
        suma += date[1]
    return(suma / len(data))

def ile_ponizej_srednia() -> int:
    srednia = oblicz_srednia(DATA)
    suma: int = 0
    for date in DATA:
        if date[1] < srednia:
            suma += 1
    return suma

def srednia_dni() -> str:
    dni: dict = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }
    for key in dni:
        dni[key] = oblicz_srednia([DATA[dzien] for dzien in range(key, len(DATA), 7)])
    return dni

def daty_temperatura() -> str:
    i = 0
    odp = []
    while i < len(DATA) - 1:
        j = i
        temp = [DATA[j-1]] if DATA[j-1][1] == DATA[j][1] else []
        while DATA[i][1] == DATA[j][1]:
            temp.append(DATA[j]) 
            j += 1
            if j > len(DATA):
                break
        i = j
        odp.append(temp)
        i += 1
    return odp

print('=' * 30 + ' zadanie 3.1 ' + '=' * 30)
wynik: list = daty_temperatura()
wynik_dlugosci = list(map(lambda x: len(x), wynik))
najwieksza_index = wynik_dlugosci.index(max(wynik_dlugosci))
print(wynik[najwieksza_index][0][0] + ' - ' + wynik[najwieksza_index][-1][0])
#FIXME: wypisuje jeden a powinien kilka największych - do naprawy
print('=' * 73)
print('=' * 30 + ' zadanie 3.3 ' + '=' * 30)
print(ile_ponizej_srednia())
print('=' * 73)
print('=' * 30 + ' zadanie 3.4 ' + '=' * 30)
wyn = srednia_dni()
for key in wyn:
    print(NAZWA_DNI[key] + ': ' + str(round(wyn[key], 2)))
print('=' * 73)