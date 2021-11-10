from matplotlib import pyplot as plt
from matplotlib import style
xYears=[2015, 2016,2017, 2018, 2019, 2020]
yDell=[1040, 1100, 1190, 1220, 1340, 1500]
yLenovo=[1000, 1050, 1120, 1200, 1300, 1400]
plt.plot(xYears, yLenovo, "g", label="line one", linewidth=5)
plt.plot(xYears, yDell, "c", label="line two", linewidth=5)
plt.title(" le prix des ordinateurs Lenovo et Dell durant les cinq dernières années")
plt.xlabel("Years")
plt.ylabel("Price")
plt.legend()
plt.grid(True, color="k")
plt.show()