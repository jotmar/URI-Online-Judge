from traceback import print_tb


nome = str(input())
salfixo = float(input())
vendidos = float(input())
print(f'TOTAL = R$ {salfixo + (vendidos / 100 * 15):.2f}')
