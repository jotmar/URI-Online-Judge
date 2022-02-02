from math import sqrt
XY = str(input()).split()
xy = str(input()).split()
for v in range(len(XY)):
    XY[v] = float(XY[v])
    xy[v] = float(xy[v])
distance = sqrt((xy[0] - XY[0])**2 + (xy[1] - XY[1])**2)
print(f'{distance:.4f}')
