from get_functional_groups import inorganic_percent, aromatic_percent, carbon_percent
import matplotlib.pyplot as plt

labels = ['inorganic', 'organic']
sizes = [inorganic_percent, 100-inorganic_percent]
colors = ['#D87608', '#EBA73B']

plt.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.title('Inorganic vs Organic molecules')
plt.show()


labels = ['Carbon based', 'non-carbon based']
sizes = [carbon_percent, 100-carbon_percent]
colors = ['#D87608', '#EBA73B']

plt.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.title('92.47% of molecules are carbon based')
plt.show()