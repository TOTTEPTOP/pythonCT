def get_sum(a, b):
    sum = a + b
    return sum

def count_capital_letters(str):
    count = 0
    for char in str:
        if char.isupper():
            count = count + 1
    return count

def decode_string(str):
    result = ""
    str.lower = str.lower()
    for char in str:
        char.lower = char.lower()
        if str_lower.count(char.lower) > 1:
            result = result + ")"
        else: 
            result = result + "("
    return result

def get_odd_count(str):
    result = 0
    for char in str:
        number = int(char)
        if number % 2 == 0:
            result = result + 1
        else:
            result = result + 0
    return result

def check_access(keycard, fingerprint, alarm, daylight):
    if alarm:
        return False
    if fingerprint:
        return True
    if keycard and daylight:
        return True
    return False