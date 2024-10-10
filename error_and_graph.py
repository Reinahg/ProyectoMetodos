import numpy as np
import matplotlib.pyplot as plt
from puntos import f
from rbf import evaluate_rbf, multiquadric_rbf, gaussian_rbf
# Este modulo calcula el error y crea la gráfica de la interpolación



def calculate_local_error(x, y, z_real, z_interp, method_name="Interpolación"):
    # Calculamos el error absoluto en cada punto
    error_abs = np.abs(z_real - z_interp)
    
    print(f"\nError absoluto en cada punto para {method_name}: {error_abs}")

# Función para graficar los resultados de la interpolación
def plot_interpolation(x, y, z_real, z_interp_mq, z_interp_gauss, title="Comparación de Superficies"):
    fig = plt.figure(figsize=(15, 9))  # Aumentamos el tamaño de la figura para acomodar varios gráficos
    
    # Crear una cuadrícula para graficar las superficies
    X, Y = np.meshgrid(x, y)
    
    # Generar Z_real para toda la cuadrícula
    Z_real_grid = np.array([[f(xi, yi) for xi in x] for yi in y])
    
    # Generar los valores interpolados para toda la cuadrícula
    Z_mq_grid = np.array([[evaluate_rbf(x, y, z_interp_mq, multiquadric_rbf, xi, yi, 1.0) for xi in x] for yi in y])
    Z_gauss_grid = np.array([[evaluate_rbf(x, y, z_interp_gauss, gaussian_rbf, xi, yi, 1.0) for xi in x] for yi in y])
    
    # 1. Gráfico de la superficie real
    ax1 = fig.add_subplot(131, projection='3d')  # 1 fila, 3 columnas, primer gráfico
    ax1.plot_surface(X, Y, Z_real_grid, cmap='Reds', alpha=0.6, edgecolor='none')
    ax1.set_title("Superficie Real")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # 2. Gráfico de la superficie interpolada multicuádrica
    ax2 = fig.add_subplot(132, projection='3d')  # 1 fila, 3 columnas, segundo gráfico
    ax2.plot_surface(X, Y, Z_mq_grid, cmap='Blues', alpha=0.6, edgecolor='none')
    ax2.set_title("Interpolada Multicuádrica")
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    
    # 3. Gráfico de la superficie interpolada gaussiana
    ax3 = fig.add_subplot(133, projection='3d')  # 1 fila, 3 columnas, tercer gráfico
    ax3.plot_surface(X, Y, Z_gauss_grid, cmap='Greens', alpha=0.6, edgecolor='none')
    ax3.set_title("Interpolada Gaussiana")
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    
    plt.suptitle(title)  # Título general para todas las gráficas
    plt.show()
