import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    """Función f(x, y) = x * e^x * sin(y)."""
    return x * np.exp(x) * np.sin(y)

def generate_grid():
    # Pedir al usuario la cantidad de valores para X y Y
    n = int(input("Ingresa la cantidad de valores para X en el intervalo [-4,0] y para Y en el intervalo [-6,3]: "))
    
    # Convertir a numpy arrays
    x_values = np.linspace(-4, 0, n)
    y_values = np.linspace(-6, 3, n)
    
    # Crear la cuadrícula usando meshgrid
    X, Y = np.meshgrid(x_values, y_values)
    
    # Evaluar la función en cada punto de la cuadrícula
    z_values = f(x_values, y_values)
    
    # Mostrar los resultados
    print("\nValores de X:")
    print(x_values)
    
    print("\nValores de Y:")
    print(y_values)
    
    print("\nValores de Z (f(x,y)):")
    print(z_values)
    
    return x_values, y_values, z_values

def plot_grid(X, Y):
    """Función para graficar la cuadrícula bidimensional X vs Y."""
    fig, ax = plt.subplots()
    
    # Graficar los puntos de la cuadrícula
    ax.scatter(X, Y, color='blue')
    
    # Conectar los puntos con líneas
    ax.plot(X, Y, 'gray', lw=1)  # Conecta las columnas de la cuadrícula
    ax.plot(X.T, Y.T, 'gray', lw=1)  # Conecta las filas de la cuadrícula
    
    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cuadrícula X-Y')
    
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

