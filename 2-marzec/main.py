# {NUMER: [OSOBY, MIASTO, [I, II, III, IV, ..., XII]]}

def read_data_file() -> dict:
    with open('dane.txt') as file:
        data_lines = file.read().rstrip().split('\n')
    data_structure = {}
    for line in data_lines[1:]:
        line_by_data = line.rstrip().split(';')
        sign = line_by_data[0]
        number = sign[:5]
        count = int(sign[5:7])
        city = sign[7:]
        data_structure[number] = [count, city, list(map(int, line_by_data[1:]))]
    return data_structure

DATA = read_data_file()
NUM_WITH_SUM = {key: sum(value[2])/value[0] for key, value in DATA.items()}
DZIELNICE = set(i[1] for i in DATA.values())

def zadanie_pierwsze():
    sorted_num_w_sum = {key: round(value, 2) for key, value in sorted(NUM_WITH_SUM.items(), key=lambda item: item[1], reverse=True)}

    for key in list(sorted_num_w_sum.keys())[:10]:
        print(key, sorted_num_w_sum[key])
print('ZADANIE 1')
zadanie_pierwsze()
print()

def zadanie_drugie():
    dzielnice_dict = {dzielnica: 0 for dzielnica in DZIELNICE}
    for key, value in DATA.items():
        city = value[1]
        dzielnice_dict[city] += sum(DATA[key][2])
    for key, value in dzielnice_dict.items():
        print(f'{key} --> {value}')
print("ZADANIE 2")
zadanie_drugie()
print()

def zadanie_trzecie():
    dzielnica_miesiacami = {dzielnica: {'I': 0, 'II': 0, 'III': 0, 'IV':0, 'V':0, 'VI': 0, 'VII': 0, 'VIII': 0, 'IX': 0, 'X': 0, 'XI': 0, 'XII': 0} for dzielnica in DZIELNICE}
    for value in DATA.values():
        city = value[1]
        usage = value[2]
        value[1]
        usage_by_month = {'I': usage[0], 'II': usage[1], 'III': usage[2], 'IV': usage[3], 'V':usage[4], 'VI': usage[5], 'VII': usage[6], 'VIII': usage[7], 'IX': usage[8], 'X': usage[9], 'XI': usage[10], 'XII': usage[11]}
        dzielnica = dzielnica_miesiacami[city]
        combined = {}
        for key in dzielnica.keys():
            combined[key] = usage_by_month[key] + dzielnica[key]
        dzielnica_miesiacami[city] = combined
    for key, value in dzielnica_miesiacami.items():
        print(f'{key} --> {max(value.values())}')
print('ZADANIE 3')
zadanie_trzecie()