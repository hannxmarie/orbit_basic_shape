import matplotlib.pyplot as plt
from graphical_visulisations import x, y, name, period, inclination
from api_calls import User, Project

# Plotting the orbit with Earth at one focus (0,0)
plt.figure(figsize=(10, 10))
plt.plot(x, y, label="Orbit Path", color='royalblue', linewidth=2)

# Adding Earth (focus)
plt.scatter([0], [0], color='orangered', s=200, label="Earth (Focus)", zorder=5)

# Adding grid and background color
plt.gca().set_facecolor('white')
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.6)

# Aspect ratio
plt.gca().set_aspect('equal', adjustable='box')

# Title and labels with custom styling
plt.title(f"{name}\nPeriod: {period} minutes, Inclination: {inclination}°\n", fontsize=14, fontweight='bold', color='darkblue')
plt.xlabel("Distance (km)", fontsize=12, color='darkslategray')
plt.ylabel("Distance (km)", fontsize=12, color='darkslategray')
plt.legend(loc='upper right', fontsize=10)
plt.savefig(f'{User}/{Project}/graph.png')
plt.show()
