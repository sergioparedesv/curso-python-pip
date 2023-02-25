import matplotlib.pyplot as plt


def plot_pie_chart(class_counts):
  categories = list(class_counts.keys())
  values = list(class_counts.values())
  plt.pie(values, labels=categories, autopct='%1.1f%%')
  plt.title('Distribución de categorías de vehículos')
  plt.savefig(f'./img/pie.png')
  return plt
