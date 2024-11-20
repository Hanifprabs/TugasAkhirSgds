import matplotlib.pyplot as plt
# Data untuk pie chart
labels = ['Apel', 'Pisang', 'Jeruk', 'Anggur']
sizes = [15, 30, 45, 10]
colors = ['yellow', 'green', 'orange', 'purple']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
