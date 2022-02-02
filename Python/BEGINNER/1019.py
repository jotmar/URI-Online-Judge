segundos = int(input())
time = {3600:0, 60:0, 1:0}
for k in time.keys():
    while segundos - k > -1:
        segundos -= k
        time[k] += 1
print(f'{time[3600]}:{time[60]}:{time[1]}')
