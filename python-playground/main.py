import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Revenue": [1000, 1200, 900, 1500],
    "Cost": [400, 500, 450, 600]
})

data["Profit"] = data["Revenue"] - data["Cost"]

print(data)
print("Total Profit:", np.sum(data["Profit"]))