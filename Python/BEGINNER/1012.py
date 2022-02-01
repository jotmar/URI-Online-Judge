values = str(input()).split()
valuesdict = {'A':float(values[0]), 'B':float(values[1]), 'C':float(values[2])}
print(f"""TRIANGULO: {valuesdict['A'] * valuesdict['C'] / 2:.3f}
CIRCULO: {3.14159 * valuesdict['C']**2:.3f}
TRAPEZIO: {(valuesdict['A'] + valuesdict['B']) / 2 * valuesdict['C']:.3f}
QUADRADO: {valuesdict['B']**2:.3f}
RETANGULO: {valuesdict['A'] * valuesdict['B']:.3f}""")
