from math import sqrt
values = str(input()).split()
result = ''
for v in range(len(values)):
    values[v] = float(values[v])
    if values[v] < 1:
        result = 'Impossivel calcular'
delta = values[1]**2 - 4 * values[0] * values[2]
if delta < 1:
    result = 'Impossivel calcular'
if result == '':
    bhaska1 = (-values[1] + sqrt(delta)) / (2 * values[0])
    bhaska2 = (-values[1] - sqrt(delta)) / (2 * values[0])
    print(f"""R1 = {bhaska1:.5f}
R2 = {bhaska2:.5f}""")
else:
    print(result)
