import numpy as np
from rbf import rbf_interpolation, multiquadric_rbf, gaussian_rbf, evaluate_rbf
from error_and_graph import calculate_local_error, plot_interpolation
from puntos import generate_grid, plot_grid

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
    
    # Evaluación de la interpolación en un nuevo punto (1.5, 2)
    x_eval, y_eval = 1.5, 2
    z_mq_eval = evaluate_rbf(x, y, coef_mq, multiquadric_rbf, x_eval, y_eval, c)
    z_gauss_eval = evaluate_rbf(x, y, coef_gauss, gaussian_rbf, x_eval, y_eval, epsilon)
    
    print(f"\nInterpolación multicuádrica en ({x_eval}, {y_eval}): {z_mq_eval}")
    print(f"Interpolación gaussiana en ({x_eval}, {y_eval}): {z_gauss_eval}")
