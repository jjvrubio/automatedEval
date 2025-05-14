import numpy as np
import matplotlib.pyplot as plt

# Data for visualization
lead_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
resource_wastage = np.array([90, 80, 70, 60, 50, 40, 30, 20, 10, 5])  # Inverted correlation

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(lead_values, resource_wastage, marker='o', linestyle='-', color='b', label="Resource Wastage vs. Lead Value")

# Labels and title
plt.xlabel("Lead Value (1 = Low, 10 = High)")
plt.ylabel("Resource Wastage (%)")
plt.title("Correlation of Lead Value vs. Resource Wastage")
plt.legend()
plt.grid(True)

# Save and display the plot
plt.savefig("/mnt/data/lead_prioritization_graph.png")
plt.show()
