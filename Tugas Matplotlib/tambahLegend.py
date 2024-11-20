import matplotlib.pyplot as plt
# Grafik dengan legenda
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

plt.plot(x, y1, color='blue', label='Data 1')
plt.plot(x, y2, color='red', label='Data 2')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Grafik dengan Legend')
plt.legend()  # Menampilkan legend
plt.show()
