value = int(input())
print(value)
notas = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
for k in notas.keys():
    while value - k  > -1:
        value -= k
        notas[k] += 1
    print(f'{notas[k]} nota(s) de R$ {k},00')
