import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into pandas dataframe
df = pd.read_csv("uzka_pro_orT01.csv")

# Plot time-energy graph
# nova radka
plt.plot(df["time"], df["KINETIC ENERGY"])
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()
