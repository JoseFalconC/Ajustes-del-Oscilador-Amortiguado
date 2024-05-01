import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Función exponencial para ajuste
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Listas para almacenar los valores de x e y
x_values = []
y_values = []

# Lee los datos desde el archivo de texto
with open("C:\\Users\\Cortez\\Downloads\\Oscilador\\Datos.txt", 'r') as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # Elimina cualquier espacio en blanco adicional alrededor de la línea
        try:
            x, y = map(float, line.split())  # Divide la línea en valores de x e y y los convierte a float
            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print(f"Error en la línea {line_number}: '{line}'")

# Grafica los valores originales
plt.plot(x_values, y_values, label='Datos Originales')

# Listas de puntos para las curvas proporcionadas [(x, y)]
data_curve1 = [(0.636, 0.244), (1.539, 0.24), (2.426, 0.237), (2.46, 0.237), (3.363, 0.236), (4.283, 0.236), (5.17, 0.234), (6.073, 0.233), (6.994, 0.233), (7.429, 0.04824), (7.88, 0.235), (8.801, 0.235), (9.704, 0.236), (10.608, 0.238), (11.511, 0.234), (12.414, 0.234), (13.318, 0.229), (14.255, 0.228), (15.142, 0.23), (16.062, 0.232), (16.948, 0.229), (17.852, 0.232), (18.755, 0.232), (19.659, 0.231), (20.562, 0.229), (21.466, 0.228), (22.386, 0.229), (23.289, 0.229), (24.193, 0.228), (25.096, 0.228), (26.0, 0.226), (26.92, 0.226), (27.823, 0.223), (28.727, 0.222), (29.63, 0.223), (30.534, 0.223), (31.437, 0.222), (32.341, 0.221), (33.244, 0.221), (34.148, 0.219), (35.068, 0.218), (35.971, 0.216), (36.875, 0.216), (37.778, 0.217), (38.698, 0.217), (39.602, 0.218), (40.505, 0.219), (41.409, 0.217), (42.312, 0.216), (43.216, 0.214), (44.119, 0.215), (45.023, 0.214), (45.943, 0.214), (46.846, 0.214), (47.75, 0.213), (48.653, 0.213), (49.557, 0.212), (50.46, 0.211), (51.364, 0.211), (52.284, 0.211), (53.17, 0.21), (54.091, 0.21), (54.994, 0.21), (55.898, 0.21), (56.801, 0.209), (57.705, 0.211), (58.608, 0.21)]
  # Reemplaza con tus datos
data_curve2 = [(1.088, 0.04797), (2.008, 0.04582), (2.443, 0.236), (2.911, 0.04451), (3.815, 0.04573), (4.718, 0.04289), (5.638, 0.04285), (6.525, 0.04619), (7.412, 0.04753), (7.445, 0.04812), (8.349, 0.04673), (9.252, 0.05129), (10.156, 0.05398), (11.076, 0.05183), (11.963, 0.05441), (12.883, 0.05162), (13.786, 0.05091), (14.69, 0.05385), (15.577, 0.0534), (16.497, 0.05628), (17.417, 0.05762), (18.304, 0.05963), (19.224, 0.06047), (20.127, 0.06133), (21.031, 0.05971), (21.934, 0.06047), (22.838, 0.06276), (23.741, 0.06336), (24.661, 0.06365), (25.548, 0.06342), (26.468, 0.06351), (27.372, 0.06342), (28.275, 0.06322), (29.179, 0.06436), (30.082, 0.06543), (31.002, 0.06384), (31.906, 0.06608), (32.809, 0.06522), (33.713, 0.06569), (34.616, 0.06546), (35.536, 0.06503), (36.44, 0.06352), (37.343, 0.06502), (38.23, 0.06665), (39.15, 0.06834), (40.054, 0.07029), (40.957, 0.07023), (41.861, 0.07037), (42.764, 0.06962), (43.667, 0.07099), (44.571, 0.07227), (45.474, 0.07304), (46.395, 0.07372), (47.298, 0.07491), (48.201, 0.07485), (49.105, 0.07587), (50.008, 0.0757), (50.929, 0.07508), (51.815, 0.07629), (52.719, 0.07763), (53.639, 0.07778), (54.542, 0.07771), (55.446, 0.07867), (56.349, 0.07847), (57.27, 0.07784), (58.173, 0.07942), (59.076, 0.07926)] # Reemplaza con tus datos

# Extraer x e y de los datos
x_curve1, y_curve1 = zip(*data_curve1)
x_curve2, y_curve2 = zip(*data_curve2)

# Ajustar la primera curva exponencial
popt1, pcov1 = curve_fit(exponential_func, x_curve1, y_curve1)

# Ajustar la segunda curva exponencial
popt2, pcov2 = curve_fit(exponential_func, x_curve2, y_curve2)

# Crear un rango de valores de x para graficar las curvas ajustadas
x_range = np.linspace(min(min(x_curve1), min(x_curve2)), max(max(x_curve1), max(x_curve2)), 100)

# Graficar la primera curva exponencial ajustada
plt.plot(x_range, exponential_func(x_range, *popt1), label='Curva Exponencial 1 Ajustada')

# Graficar la segunda curva exponencial ajustada
plt.plot(x_range, exponential_func(x_range, *popt2), label='Curva Exponencial 2 Ajustada')

# Etiquetas y leyenda
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Descripción del Movimiento Armónico')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir las ecuaciones ajustadas
print("Ecuación de la Curva Exponencial 1:")
print(f"y = {popt1[0]} * exp(-{popt1[1]} * x) + {popt1[2]}")

print("\nEcuación de la Curva Exponencial 2:")
print(f"y = {popt2[0]} * exp(-{popt2[1]} * x) + {popt2[2]}")
