import numpy as np
import matplotlib.pyplot as plt

# Define two vectors
a = np.array([1, 3])
b = np.array([2, -2])

# Add them
a_plus_b = a + b
print("a + b =", a_plus_b)

# Multiply by scalar
scaled_a = 3 * a
print("3a =", scaled_a)

# Multiply them
dot_product = np.dot(a, b)
print("a · b =", dot_product)

# Plot them
origin = [0, 0]

plt.quiver(*origin, *a, color='blue', scale=1, scale_units='xy', angles='xy', label='a')
plt.quiver(*origin, *b, color='red', scale=1, scale_units='xy', angles='xy', label='b')
plt.quiver(*origin, *a_plus_b, color='green', scale=1, scale_units='xy', angles='xy', label='a+b')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title("Vector Addition")
plt.show()




