import numpy as np
from rbf import rbf_interpolation, multiquadric_rbf, gaussian_rbf, evaluate_rbf

if __name__ == "__main__":
    # Puntos de entrada
    x = np.array([0, 1, 2])
    y = np.array([0, 1, 4])
    z = np.array([0, 1, 2])
    
    # Parámetros para las funciones de base radial
    c = 1.0  # Parámetro para multicuádrica
    epsilon = 1.0  # Parámetro para gaussiana
    
    # Interpolación multicuádrica
    print("Interpolación Multicuádrica:")
    coef_mq, A_mq = rbf_interpolation(x, y, z, multiquadric_rbf, c)
    
    # Interpolación gaussiana
    print("\nInterpolación Gaussiana:")
    coef_gauss, A_gauss = rbf_interpolation(x, y, z, gaussian_rbf, epsilon)
    
    # Evaluación de la interpolación en un nuevo punto (1.5, 2)
    x_eval, y_eval = 1.5, 2
    z_mq_eval = evaluate_rbf(x, y, coef_mq, multiquadric_rbf, x_eval, y_eval, c)
    z_gauss_eval = evaluate_rbf(x, y, coef_gauss, gaussian_rbf, x_eval, y_eval, epsilon)
    
    print(f"\nInterpolación multicuádrica en ({x_eval}, {y_eval}): {z_mq_eval}")
    print(f"Interpolación gaussiana en ({x_eval}, {y_eval}): {z_gauss_eval}")
