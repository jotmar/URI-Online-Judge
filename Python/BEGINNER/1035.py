valores = str(input()).split()
for v in range(len(valores)):
    valores[v] = int(valores[v])
if valores[1] > valores[2] and valores[3] > valores[0] and valores[2] + valores[3] > valores[0] + valores[1] and valores[0] >= 0 and valores[2] > 0 and valores[3] > 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
