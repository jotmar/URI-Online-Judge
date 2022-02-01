values = str(input()).split()
a = int(values[0])
b = int(values[1])
c = int(values[2])
MaiorAB = (a+b+abs(a-b))/2
print(f'{(MaiorAB+c+abs(MaiorAB-c))/2:.0f} eh o maior')
