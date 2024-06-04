import matplotlib.pyplot as plt

# For the title of the chart
# String
# Text Color
# Font Size
# Vertical Alignment
# Vertical Positioning
plt.title('Progress Grid', color ="blue", size=14, loc="left", y=0.3)

# For the x axis
plt.xlabel("Years passed")

# For the y axis
# rotation is for rotating the label
plt.ylabel('Runs taken', rotation=90)

plt.show()