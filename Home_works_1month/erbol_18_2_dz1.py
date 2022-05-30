obl1 = input('Область 1 : ')
obl2 = input('Область 2 : ')
obl3 = input('Область 3 : ')
obl4 = input('Область 4 : ')
obl5 = input('Область 5 : ')
obl6 = input('Область 6 : ')
obl7 = input('Область 7 : ')

allObl = int(obl1) + int(obl2) + int(obl3) + int(obl4) + int(obl5) + int(obl6) + int(obl7)

average = allObl / 7

print(average)

print(f'Средний показатель температуры воздуха по КР на сегодня: {round(average, 1)} ')
