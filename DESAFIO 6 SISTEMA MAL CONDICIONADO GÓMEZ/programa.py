import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz A y el vector b
A = np.array([[2, 4, 5], [6, 9, 8], [4.1, 5, 3]])
b = np.array([220, 490, 274])

# Resolver el sistema
x = np.linalg.solve(A, b)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear una malla de puntos
X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))

# Definir las ecuaciones del plano
Z1 = (220 - 2*X - 4*Y) / 5
Z2 = (490 - 6*X - 9*Y) / 8
Z3 = (274 - 4.1*X - 5*Y) / 3

# Graficar los planos
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100)

# Mostrar la solución
ax.scatter(x[0], x[1], x[2], color='r', s=100)

plt.show()
