def get_data() -> list:
    """
        funkcja zwraca tablicę tablic z ['data', temperatura]
    """
    with open('temperatury_nowy_york.txt') as file: #otwiera plik
        file: list = file.read().split('\n') #odczytuje plik i dzieli go po nowych liniach
    data: list = list(map(lambda x: x.split(' '), file)) #tworzy tablicę tablic ['data', 'temperatura']
    for date in data: #zmienia każdą temperaturę na liczbę
        date[1] = int(date[1])
    return data

#stała z danymi z pliku
DATA: list = get_data()
#stała z dniami tygodnia zaczynając od piątku - potrzebne do zadania
NAZWA_DNI: dict = {
    0: 'piątek',
    1: 'sobota',
    2: 'niedziela',
    3: 'poniedziałek',
    4: 'wtorek',
    5: 'środa',
    6: 'czwartek',
}

oblicz_srednia = lambda data: sum(date[1] for date in data) / len(data) #oblicza średnią z całego okresu zapisu

def ile_ponizej_srednia() -> int:
    """
        funkcja zwraca INT - liczbę temperatur poniżej średniej
    """
    srednia = oblicz_srednia(DATA)
    #tworzy tablicę z wartością True wtedy kiedy temperatura jest poniżej średniej
    return sum(date[1] < srednia for date in DATA)

#funkcja oblicza srednią z każdego dnia, zwraca DICT {numer_dnia: średnia}
srednia_dni = {key: oblicz_srednia([DATA[dzien] for dzien in range(key, len(DATA), 7)]) for key in range(7)}

def daty_temperatura() -> None:
    """
        funkcja wypisuje najdłuższy zakres dat z tą samą temperaturą
    """
    i = 0 #index początkowy, zmienna pomocnicza
    odp = [] #odpowiedź, będzie to tablica tablic zawierającymi tablicę z datą i temperaturą (tablica trójwymiarowa)
    while i < len(DATA) - 1: #dopóki i jest mniejsze od długości DATA
        j = i #druga zmienna pomocnicza, przechodzi od aktualnej do ostatniej tablicy z tą samą temperaturą
        temp = [DATA[j-1]] if DATA[j-1][1] == DATA[j][1] else [] #tablica pomocnicza, poprzednia tablica, ponieważ był jakiś bug, że w jednym przypadku nie działało
        while DATA[i][1] == DATA[j][1]: #dopóki temperatury są takie same
            temp.append(DATA[j]) #dodaj tablicę do listy pomocniczej
            j += 1 
            if j > len(DATA): #bug, że na końcu wywalało program, jeżeli jest ponad długość tablicy przerywa pętle
                break
        i = j + 1 #kontynuujemy od ostatniego sprawdzonego indeksu
        odp.append(temp)
    odp_dlug = list(map(len, odp)) #lista z długościami list
    wynik = [odp[i] for i in range(len(odp_dlug)) if odp_dlug[i] == max(odp_dlug)] #lista z najdłuższymi okresami
    for w in wynik: #wypisuje zakres dat wszystkich najdłuższych okresów
        print(w[0][0] + ' - ' + w[-1][0])

def rosnaca_temperatura():
    """
        funkcja wypisuje najdłuższy zakres dat z niemalejącą temperaturą
    """
    i = 0
    odp = []
    while i < len(DATA) - 1: 
        j = i
        temp = []
        while DATA[j][1] >= DATA[j - 1][1]: #NOTE: zmiana - dopóki teraźniejsza temperatura jest mniejsza lub równa od poprzedniej
            temp.append(DATA[j])
            if j + 1 >= len(DATA) - 1: #bug, który wywalał błąd z za dużą zmienną j
                break
            j += 1
        i = j + 1
        odp.append(temp)
    odp_dlug = list(map(len, odp))
    wynik = [odp[i] for i in range(len(odp_dlug)) if odp_dlug[i] == max(odp_dlug)]
    for w in wynik:
        print(w[0][0] + ' - ' + w[-1][0]) #NOTE: wszystko inne jak wyżej

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