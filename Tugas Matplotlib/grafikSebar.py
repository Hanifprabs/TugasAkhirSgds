import matplotlib.pyplot as plt
# Data untuk grafik sebar
x = [1, 2, 3, 4, 5]
y = [5, 4, 6, 7, 8]

plt.scatter(x, y, color='red', marker='o')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Grafik Sebar')
plt.show()
