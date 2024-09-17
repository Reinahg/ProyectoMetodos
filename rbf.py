import numpy as np
# Este módulo construye la matriz de coheficientes y 
# el vector de terminos independientes

# Función de base radial Multicuádrica
def multiquadric_rbf(r, c=1.0):
    return np.sqrt(r**2 + c**2)

# Función de base radial Gaussiana
def gaussian_rbf(r, epsilon=1.0):
    return np.exp(-(epsilon**2) * r**2)

# Cálculo de la matriz de distancias entre puntos
def calculate_distance_matrix(x, y):
    # Creamos una matriz vacía de distancias
    n = len(x)
    dist_matrix = np.zeros((n, n))
    
    # Calculamos la distancia euclidiana entre todos los pares de puntos
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    
    return dist_matrix

# Interpolación usando RBF
def rbf_interpolation(x, y, z, rbf_function, *params):
    # Número de puntos
    n = len(x)
    
    # Calculamos la matriz de distancias
    dist_matrix = calculate_distance_matrix(x, y)
    
    # Evaluamos la función RBF sobre la matriz de distancias
    A = rbf_function(dist_matrix, *params)
    
    # Imprimimos la matriz de coeficientes (A)
    print("Matriz de coeficientes (A):")
    print(A)
    
    # Imprimimos el vector de términos independientes (z)
    print("\nVector de términos independientes (z):")
    print(z)
    
    # Resolvemos el sistema A * coef = z para obtener los coeficientes
    coef = np.linalg.solve(A, z)
    
    # Imprimimos el vector de coeficientes (coef)
    print("\nVector de coeficientes (coef):")
    print(coef)
    
    return coef, A

# Evaluación de la interpolación en un punto nuevo (x_eval, y_eval)
def evaluate_rbf(x, y, coef, rbf_function, x_eval, y_eval, *params):
    # Calculamos la distancia desde el nuevo punto a los puntos originales
    dist_eval = np.sqrt((x - x_eval)**2 + (y - y_eval)**2)
    
    # Aplicamos la función RBF a las distancias
    phi_eval = rbf_function(dist_eval, *params)
    
    # Calculamos la interpolación como la combinación lineal de las RBF evaluadas
    # La funcion producto punto (np.dot) es la encargada de multiplicar el coheficiente con 
    # psi (Ψ) e irlos sumando creando la sumatoria de la función
    z_eval = np.dot(coef, phi_eval)
    
    return z_eval