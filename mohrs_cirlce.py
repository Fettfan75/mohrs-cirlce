import numpy as np
import matplotlib.pyplot as plt

def mohrs_circle(sigma_x, sigma_y, tau_xy):
    # Center of the circle (C)
    center = (sigma_x + sigma_y) / 2

    # Radius of the circle (R)
    radius = np.sqrt(((sigma_x - sigma_y) / 2)**2 + tau_xy**2)

    # Principal stresses (σ1 and σ2)
    principal_stresses = (center + radius, center - radius)

    # Maximum shear stress (τ_max)
    max_shear_stress = radius

    # Plotting Mohr's Circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center + radius * np.cos(theta)
    y = radius * np.sin(theta)

    plt.figure()
    plt.plot(x, y, label="Mohr's Circle")
    plt.scatter([sigma_x, sigma_y], [tau_xy, -tau_xy], color='red') # Points for sigma_x, sigma_y
    plt.xlabel('Normal Stress')
    plt.ylabel('Shear Stress')
    plt.grid()
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.show()

    return {
        'Center (C)': center,
        'Radius (R)': radius,
        'Principal Stresses': principal_stresses,
        'Maximum Shear Stress': max_shear_stress
    }

# Example usage
sigma_x = 50
sigma_y = 100
tau_xy = 30
results = mohrs_circle(sigma_x, sigma_y, tau_xy)

for key, value in results.items():
    print(f"{key}: {value}")

