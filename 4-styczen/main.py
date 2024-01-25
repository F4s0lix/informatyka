def get_data() -> list:
    with open('temperatury_nowy_york.txt') as file:
        file: list = file.read().split('\n')
    data: list = list(map(lambda x: x.split(' '), file)) #tablica tablic z datą i temperaturą
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

oblicz_srednia = lambda data: sum(date[1] for date in data) / len(data)

def ile_ponizej_srednia() -> int:
    srednia = oblicz_srednia(DATA)
    return sum(date[1] < srednia for date in DATA)

srednia_dni = lambda: {key: oblicz_srednia([DATA[dzien] for dzien in range(key, len(DATA), 7)]) for key in range(7)}

def daty_temperatura() -> None:
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
        i = j + 1
        odp.append(temp)
    
    odp_dlug = list(map(len, odp))
    wynik = [odp[i] for i in range(len(odp_dlug)) if odp_dlug[i] == max(odp_dlug)]
    for w in wynik:
        print(w[0][0] + ' - ' + w[-1][0])

def rosnaca_temperatura():
    i = 0
    odp = []
    while i < len(DATA) - 1:
        j = i
        temp = []
        while DATA[j][1] >= DATA[j - 1][1]:
            temp.append(DATA[j])
            if j + 1 >= len(DATA) - 1:
                break
            j += 1
        i = j + 1
        odp.append(temp)
    odp_dlug = list(map(len, odp))
    wynik = [odp[i] for i in range(len(odp_dlug)) if odp_dlug[i] == max(odp_dlug)]
    for w in wynik:
        print(w[0][0] + ' - ' + w[-1][0])

print('=' * 30 + ' zadanie 3.1 ' + '=' * 30)
daty_temperatura()
print('=' * 73)
print('=' * 30 + ' zadanie 3.2 ' + '=' * 30)
rosnaca_temperatura()
print('=' * 73)
print('=' * 30 + ' zadanie 3.3 ' + '=' * 30)
print(ile_ponizej_srednia())
print('=' * 73)
print('=' * 30 + ' zadanie 3.4 ' + '=' * 30)
wyn = srednia_dni()
for key in wyn:
    print(NAZWA_DNI[key] + ': ' + str(round(wyn[key], 2)))
print('=' * 73)