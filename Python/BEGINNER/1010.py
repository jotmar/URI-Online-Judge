produto1 = str(input()).split()
produto2 = str(input()).split()
for p in range(len(produto1)):
    produto1[p] = float(produto1[p])
for p in range(len(produto2)):
    produto2[p] = float(produto2[p])
print(f'VALOR A PAGAR: R$ {(produto1[1] * produto1[2]) + (produto2[1] * produto2[2]):.2f}')
