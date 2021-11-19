import matplotlib.pyplot as plt

year = [2000, 2005, 2010, 2015, 2020]
sgp  = [3, 4, 5, 6, 7]
ind = [7, 8, 9, 10, 11]

plt.plot(year, sgp, color='green')
plt.plot(year, ind, color='orange')
plt.xlabel('GDP')
plt.ylabel('Countries')
plt.title('BofA Title')
plt.show()
