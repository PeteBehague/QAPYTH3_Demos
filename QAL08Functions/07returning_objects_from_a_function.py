def calc_vat(gross, vatpc=17.5):
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   return [f'{net:05.2f}', f'{vat:05.2f}']

def asterisk_adder(val1, val2, val3):
    val1 += "*"
    val2 += "*"
    val3 += "*"
    return val1, val2, val3

result = calc_vat(42.30)
print(calc_vat(9.55))

v1, v2, v3 = asterisk_adder('a', 'b', 'c')
print(f"v1: {v1}, v2: {v2}, v3: {v3}")
