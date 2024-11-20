import matplotlib.pyplot as plt
# Grafik sebar dengan warna dan marker
x = [1, 2, 3, 4, 5]
y = [5, 4, 6, 7, 8]

plt.scatter(x, y, color='blue', marker='x', label='Data 1')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Grafik dengan Warna dan Marker')
plt.legend()
plt.show()
