from calendar import calendar, month
import random

sales = [random.randint(10000, 20000) for _ in range(12)]

print("Monthly sales:", sales)

mean = sum(sales) / len(sales)
print("Mean sales:", mean)

squared_diffs = []

for value in sales:
    diff = value - mean
    squared = diff ** 2
    squared_diffs.append(squared)

variance = sum(squared_diffs) / len(sales)

print("Variance:", variance)

std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)

max_value = max(sales)
max_index = sales.index(max_value)

print ("Highest sales month", max_index + 1, "with sales of", max_value)

cv = std_dev / mean
print("Coefficient of Variation:", cv)