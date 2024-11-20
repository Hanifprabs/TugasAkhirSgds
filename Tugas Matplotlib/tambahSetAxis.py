import matplotlib.pyplot as plt
# Grafik batang dengan set axis
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.xlabel('Kategori')
plt.ylabel('Nilai')
plt.title('Grafik Batang dengan Set Axis')
plt.axis([-1, 4, 0, 10])  # Mengatur batas axis (xmin, xmax, ymin, ymax)
plt.show()
