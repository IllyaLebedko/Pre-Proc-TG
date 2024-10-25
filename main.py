a = [0.025, 0.05, 0.075]
b = [1.64, 1.64, 1.64]

def squareTriangle():
    firstBraсket = a[0]*b[1]+a[1]*b[2]+a[2]*b[0]
    secondBraсket = b[0]*a[1]+b[1]*a[2]+b[2]*a[0]
    return (firstBraсket-secondBraсket)/2

a = squareTriangle()
print(a)