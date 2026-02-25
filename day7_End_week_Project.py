
import calendar
import random

growth_rate = 0.05 # 5% growth rate

revenue = {}

# first month random
previous_revenue = random.randint(3200, 3800)

for month in calendar.month_name[1:]:
    revenue[month] = previous_revenue
    previous_revenue = int(previous_revenue * (1 + growth_rate))

for month, rev in revenue.items():
    print(month, ":", rev, 2)\

sum_revenue = sum(revenue.values())
average_revenue = sum_revenue / len(revenue)
variance = sum((rev - average_revenue) ** 2 for rev in revenue.values()) / len(revenue)
std_dev = variance ** 0.5
print("Average monthly revenue:", round(average_revenue, 2))
print("Variance:", round(variance, 2))
print("Standard deviation:", round(std_dev, 2))
print("Total revenue for the year:", round(sum_revenue, 2))



