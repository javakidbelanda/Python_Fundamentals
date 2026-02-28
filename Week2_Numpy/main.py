import numpy as np

# Create array
data = np.array([10, 20, 30, 40, 50])

print("Data:", data)

# Basic analytics
print("Mean:", np.mean(data))
print("Standard deviation:", np.std(data))
print("Sum:", np.sum(data))

# Vectorized operation
profit = data * 1.2

print("Profit projection (+20%):", profit)