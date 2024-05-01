import matplotlib.pyplot as plt

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

# Grafica los valores
plt.plot(x_values, y_values)
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Descripción del Movimiento Armónico')
plt.grid(True)
plt.show()
