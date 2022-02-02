days = int(input())
age = {365:0, 30:0, 1:0}
for k in age.keys():
    while days - k > -1:
        days -= k
        age[k] += 1
print(f"""{age[365]} ano(s)
{age[30]} mes(es)
{age[1]} dia(s)""")
