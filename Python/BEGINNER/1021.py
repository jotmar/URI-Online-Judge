valor = float(input())
notas = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}
moedas = {1.00:0, 0.50:0, 0.25:0, 0.10:0, 0.05:0, 0.01:0}
print('NOTAS:')
for k in notas.keys():
    while valor - k >= 0:
        valor -= k
        notas[k] += 1
    print(f'{notas[k]} nota(s) de R$ {k}.00')
print('MOEDAS:')
for k in moedas.keys():
    while valor - k >= 0:
        valor -= k
        moedas[k] += 1
    print(f'{moedas[k]} moeda(s) de R$ {k:.2f}')
