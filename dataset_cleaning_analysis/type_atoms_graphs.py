# from get_functional_groups import inorganic_percent, aromatic_percent
import matplotlib.pyplot as plt



labels = ['inorganic', 'organic']
sizes = [6.7, 100-6.7]
colors = ['#46599E', '#A4B1FF']

plt.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%', startangle=180, textprops={'fontsize': 14})
plt.axis('equal')
plt.title('Inorganic vs Organic molecules',fontsize=18)
plt.show()


# labels = ['Carbon based', 'non-carbon based']
# sizes = [carbon_percent, 100-carbon_percent]
# colors = ['#D87608', '#EBA73B']

# plt.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%', startangle=180)
# plt.axis('equal')
# plt.title('92.47% of molecules are carbon based')
# plt.show()



# labels = ['Aromatic', 'non-aromatic organic molecules']
# sizes = [aromatic_percent, 100-aromatic_percent]
# colors = ['#D87608', '#EBA73B']

# plt.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%', startangle=180, textprops={'fontsize': 14})
# plt.axis('equal')
# plt.title('23.2% of organic SMILE molecules have an aromatic group',fontsize=18)
# plt.show()