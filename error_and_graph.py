import numpy as np
import matplotlib.pyplot as plt
# Este modulo calcula el error y crea la gráfica de la interpolación


def calculate_local_error(x, y, z_real, z_interp, method_name="Interpolación"):
    # Calculamos el error absoluto en cada punto
    error_abs = np.abs(z_real - z_interp)
    
    print(f"\nError absoluto en cada punto para {method_name}: {error_abs}")

# Función para graficar los resultados de la interpolación
def plot_interpolation(x, y, z_real, z_interp_mq, z_interp_gauss, title="Interpolación"):
    fig = plt.figure(figsize=(10, 6))
    
    # Gráfica de los puntos reales y los puntos interpolados, conectados por líneas
    ax = fig.add_subplot(111, projection='3d')
    
    # Puntos reales (en rojo)
    ax.scatter(x, y, z_real, color='r', label="Puntos Reales", s=50)
    
    # Puntos interpolados multicuádricos (en azul)
    ax.scatter(x, y, z_interp_mq, color='b', label="Interpolados Multicuádrica", s=50)
    
    # Puntos interpolados gaussianos (en verde)
    ax.scatter(x, y, z_interp_gauss, color='g', label="Interpolados Gaussiana", s=50)
    
    # Conectar los puntos reales con los interpolados multicuádricos mediante líneas
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [y[i], y[i]], [z_real[i], z_interp_mq[i]], color='gray', linestyle='--')
    
    # Conectar los puntos reales con los interpolados gaussianos mediante líneas
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [y[i], y[i]], [z_real[i], z_interp_gauss[i]], color='lightgreen', linestyle='--')
    
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.legend()
    
    plt.show()