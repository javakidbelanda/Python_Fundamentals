# Day 2 - Funcntion & Structure

def compund_formula(principal, rate, years):
    amount = principal
    ratte = rate

    for i in range(years):
        amount = amount + (amount * ratte)
        ratte = ratte + 0.02

        print("Year", i + 1, "Amount", amount)

    return amount
    

result = compund_formula(1000, 0.05, 10)
    

  

   



