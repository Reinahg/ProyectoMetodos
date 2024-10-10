import numpy as np
from rbf import rbf_interpolation, multiquadric_rbf, gaussian_rbf, evaluate_rbf
from error_and_graph import calculate_local_error, plot_interpolation
from puntos import generate_grid, plot_grid, f
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Para encontrar los máximos de la función f(x, y), 
# derivamos la función en ambas variables x e y, y 
# luego resolvemos el sistema de ecuaciones resultantes 
# para los puntos donde las derivadas parciales sean cero.
def find_extrema():
    # Función que queremos minimizar (encontrar extremos)
    func_to_minimize = lambda vars: -f(vars[0], vars[1])  # Ponemos -f para buscar máximos
    
    # Valor inicial aleatorio
    initial_guess = [0, 0]  # SUPONEMOS que empezamos en (0, 0), esto puede cambiar

    # Método L-BFGS-B para minimizar la función
    result = minimize(func_to_minimize, initial_guess, bounds=[(-4, 0), (-6, 3)])

    # Extrae las coordenadas del extremo y el valor máximo encontrado
    x_ext, y_ext = result.x
    z_ext = f(x_ext, y_ext)

    print(f"\nMáximo aproximado de la función f(x,y) en: x = {x_ext:.4f}, y = {y_ext:.4f}, z = {z_ext:.4f}")
    
    return x_ext, y_ext, z_ext  # Devolvemos el punto (x, y) y el valor z correspondiente

if __name__ == "__main__":
    print("\nEste codigo construye dos funciones de interpolación para aproximar la superficie generada por la función 𝑓(𝑥, 𝑦) utilizando interpolación con funciones de base radial de dos tipos: multicuádrica y Gaussiana\n")
    
    # Puntos de entrada
    x, y, z_real = generate_grid()
    X, Y = np.meshgrid(x, y)
    plot_grid(X,Y)
    
    # Parámetros para las funciones de base radial
    c = 1.0  # Parámetro para multicuádrica
    epsilon = 1.0  # Parámetro para gaussiana
    
    # Interpolación multicuádrica
    print("Interpolación Multicuádrica:")
    coef_mq, A_mq = rbf_interpolation(x, y, z_real, multiquadric_rbf, c)
    
    # Interpolación gaussiana
    print("\nInterpolación Gaussiana:")
    coef_gauss, A_gauss = rbf_interpolation(x, y, z_real, gaussian_rbf, epsilon)
    
    # Evaluación de la interpolación en el mismo conjunto de puntos
    z_interp_mq = np.array([evaluate_rbf(x, y, coef_mq, multiquadric_rbf, xi, yi, c) for xi, yi in zip(x, y)])
    z_interp_gauss = np.array([evaluate_rbf(x, y, coef_gauss, gaussian_rbf, xi, yi, epsilon) for xi, yi in zip(x, y)])

    # Cálculo del error
    calculate_local_error(x, y, z_real, z_interp_mq, method_name="Multicuádrica")
    calculate_local_error(x, y, z_real, z_interp_gauss, method_name="Gaussiana")
    
    # Graficar los resultados comparados
    plot_interpolation(x, y, z_real, z_interp_mq, z_interp_gauss, title="Comparación de Interpolaciones")
    
    #Codigo para encontrar los valores extremos
    x_ext, y_ext, _ = find_extrema()
    
    # Evaluamos la interpolación multicuádrica en el punto extremo
    z_mq_ext = evaluate_rbf(x, y, coef_mq, multiquadric_rbf, x_ext, y_ext, c)

    # Evaluamos la interpolación gaussiana en el punto extremo
    z_gauss_ext = evaluate_rbf(x, y, coef_gauss, gaussian_rbf, x_ext, y_ext, epsilon)

    print(f"\nInterpolación Multicuádrica en punto extremo ({x_ext}, {y_ext}): {z_mq_ext}")
    print(f"Interpolación Gaussiana en punto extremo ({x_ext}, {y_ext}): {z_gauss_ext}")
    
    # Valor real f(x_ext, y_ext)
    z_ext_real = f(x_ext, y_ext)

    # Calculamos los errores locales de las interpolaciones
    error_mq_ext = np.abs(z_ext_real - z_mq_ext)
    error_gauss_ext = np.abs(z_ext_real - z_gauss_ext)

    print(f"\nError en la interpolación multicuádrica en ({x_ext}, {y_ext}): {error_mq_ext}")
    print(f"Error en la interpolación gaussiana en ({x_ext}, {y_ext}): {error_gauss_ext}")

    # Gráfico de barras

    names = ['Multicuádrica', 'Gaussiana']
    errors = [error_mq_ext, error_gauss_ext]

    plt.bar(names, errors, color=['blue', 'green'])
    plt.title(f"Errores locales en las interpolaciones en el punto extremo ({x_ext:.2f}, {y_ext:.2f})")
    plt.ylabel('Error absoluto')
    plt.show()
        
    



