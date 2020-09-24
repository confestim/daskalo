# add threshold of division by the second polynomial
import numpy as np
x = np.array([1,7,18,20,8])
y = np.array([1,2,1])

print(f"Stepen na rezultata {len(x)-len(y)}")
pedal, pedal2 = np.polydiv(x,y)
pedalList = list(pedal)
pedal2List = list(pedal2)

a = list(map(int, range(len(pedalList))))
a = a[::-1]

print("Rezultat:")
for i in range(len(pedalList)):
    print(f"{int(pedalList[i])}x^{a[i]}")

b = list(map(int, range(len(pedal2List)))) 
b = b[::-1]

print("Ostatuk")
for i in range(len(pedal2List)):
    print(f"{int(pedal2List[i])}x^{b[i]}")
