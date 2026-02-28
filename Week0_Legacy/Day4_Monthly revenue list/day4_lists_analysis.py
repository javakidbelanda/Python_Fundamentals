monthly_data = {
    "January": 12000,
    "February": 15000,
    "March": 11000,
    "April": 18000
}
def analyze_monthly_data(data, threshold):
    if not data:
        print("No data provided.")
        return

    total_revenue = sum(data.values())
    best_month = max(data, key=data.get)
    print("Total revenue for the year:", total_revenue)
    print("Best month:", best_month, "with", data[best_month])
    
    print("Months with revenue above", threshold, ":")
    for month, revenue in data.items():
        if revenue > threshold:
            print("-",month, ":", revenue)

result = analyze_monthly_data(monthly_data, 14000)
    
    