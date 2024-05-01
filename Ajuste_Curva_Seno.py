import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Función sinusoidal amortiguada: f(x) = A * exp(-x / tau) * sin(2 * pi * f * x + phi)
def damped_sine(x, A, tau, f, phi):
    return A * np.exp(-x / tau) * np.sin(2 * np.pi * f * x + phi)

# Cargar datos desde el archivo de texto
try:
    data = np.loadtxt("datos.txt")
except FileNotFoundError:
    print("¡Error! No se pudo encontrar el archivo 'datos.txt'.")
    exit()

# Separar los datos en x y y
x_data = data[:, 0]
y_data = data[:, 1]

# Realizar el ajuste con valores iniciales adecuados y un máximo de 10000 iteraciones
try:
    popt, pcov = curve_fit(damped_sine, x_data, y_data, p0=(1, 1, 1, 0), maxfev=10000)
except RuntimeError as e:
    print("¡Error durante el ajuste:", e)
    exit()

# Generar los valores predichos a partir del ajuste
y_fit = damped_sine(x_data, *popt)

# Desplazar la ecuación en 0.15 unidades positivas en el eje y
y_fit += 0.14

# Graficar los datos y el ajuste
plt.scatter(x_data, y_data, label='Datos')
plt.plot(x_data, y_fit, 'r-', label='Ajuste seno amortiguado')
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
plt.title('Ajuste a una Función Seno Amortiguada')
plt.legend()
plt.grid(True)
plt.autoscale(enable=True, axis='x', tight=True)  # Ajusta la escala del eje x automáticamente
plt.show()

# Coeficientes del ajuste (A, tau, f, phi)
A, tau, f, phi = popt
print("Coeficientes del ajuste:")
print("Amplitud (A):", A)
print("Constante de tiempo (tau):", tau)
print("Frecuencia (f):", f)
print("Fase (phi):", phi)

