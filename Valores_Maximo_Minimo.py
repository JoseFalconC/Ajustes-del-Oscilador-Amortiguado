import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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

# Encuentra picos máximos y mínimos
peaks_max, _ = find_peaks(y_values, prominence=0)
peaks_min, _ = find_peaks([-y for y in y_values], prominence=0)

# Lista de puntos máximos
max_points = [(x_values[i], y_values[i]) for i in peaks_max]
# Lista de puntos mínimos
min_points = [(x_values[i], y_values[i]) for i in peaks_min]

print("Puntos máximos:", max_points)
print("Puntos mínimos:", min_points)

