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
print('=' * 30 + ' zadanie 3.3 ' + '=' * 30)
print(ile_ponizej_srednia())
print('=' * 73)
print('=' * 30 + ' zadanie 3.4 ' + '=' * 30)
wyn = srednia_dni()
for key in wyn:
    print(NAZWA_DNI[key] + ': ' + str(round(wyn[key], 2)))
print('=' * 73)