import requests


def convert_brl_to_euro(value):
    response = requests.get('https://api.fixer.io/latest?symbols=EUR&base=BRL')
    data = response.json()
    rate = data['rates']['EUR']
    converted = value / rate
    if rate < 4:
        total = converted * 0.7
    else:
        total = converted * 0.8

    return total


# path-count: 2 + 1-ish (requests)
# total: ~3 tests
# mocks: ~3 (all tests)



# isolate I/O

def get_euro_rate():
    pass


def convert_brl_to_euro_v2(value):
    rate = get_euro_rate()
    converted = value / rate
    if rate < 4:
        total = converted * 0.7
    else:
        total = converted * 0.8

    return total


# path-count: 2 + 1-ish (get_euro_rate error)
# get_euro_rate: requests 2-ish
# total: ~5 tests
# mocks: ~5 (all, but distinct)



# promote I/O

def calculate_conversion(value, rate):
    converted = value / rate
    if rate < 4:
        total = converted * 0.7
    else:
        total = converted * 0.8

    return total

def convert_brl_to_euro_v3(value):
    response = requests.get('https://api.fixer.io/latest?symbols=EUR&base=BRL')
    data = response.json()
    return calculate_conversion(value, data['rates']['URL'])


# path-count: 1 + 1-ish (requests)
# calculate_conversion: 2 (path-count)
# total: ~4
# mocks: ~2 (only convert_brl_to_euro)
