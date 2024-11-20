import matplotlib.pyplot as plt

# Data untuk grafik batang
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values, color='blue')
plt.xlabel('Kategori')
plt.ylabel('Nilai')
plt.title('Grafik Batang')
plt.show()
