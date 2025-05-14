import numpy as np
import matplotlib.pyplot as plt

# Data for visualization: A/B Testing Performance
variants = ["Variant A", "Variant B", "Variant C", "Variant D"]
click_through_rates = [12, 18, 25, 30]  # Hypothetical CTR values (%)
response_rates = [8, 14, 20, 24]  # Hypothetical Response Rates (%)

# Creating the bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bar_width = 0.35
index = np.arange(len(variants))

# Plot Click-Through Rates
bar1 = ax.bar(index, click_through_rates, bar_width, label="Click-Through Rate (%)", alpha=0.7)

# Plot Response Rates
bar2 = ax.bar(index + bar_width, response_rates, bar_width, label="Response Rate (%)", alpha=0.7)

# Labels and Title
ax.set_xlabel("Message Variants")
ax.set_ylabel("Performance Metrics (%)")
ax.set_title("A/B Testing Results: Click-Through and Response Rates")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(variants)
ax.legend()

# Save and display the chart
plt.tight_layout()
plt.savefig("/mnt/data/ab_testing_results.png")
plt.show()
