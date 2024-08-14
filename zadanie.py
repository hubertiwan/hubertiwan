import matplotlib.pyplot as plt
import numpy as np

# Parametry
D = 1  # dowolna jednostka długości
S = 1  # dowolna jednostka szybkości transmisji

# Wartości I od 0 do 0.99 (unikając I = 1, ponieważ prowadzi to do nieskończoności)
I = np.linspace(0, 0.99, 1000)

# Całkowite opóźnienie
D_cal = D / (S * (1 - I))

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(I, D_cal, label=r'$D_{\text{całkowite}} = \frac{D}{S(1-I)}$')
plt.xlabel(r'$I$ (Natężenie ruchu)')
plt.ylabel(r'$\frac{D}{S}$ (Całkowite opóźnienie)')
plt.title('Całkowite opóźnienie w funkcji natężenia ruchu')
plt.grid(True)
plt.legend()
plt.ylim(0, 10)  # ograniczenie y dla lepszego widoku
plt.show()
