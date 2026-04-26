import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Simulate Healthy Vibration (Smooth sine wave + low noise)
t = np.linspace(0, 1, 1000)
healthy = np.sin(2 * np.pi * 50 * t) + np.random.normal(0, 0.2, 1000)

# 2. Simulate Faulty Vibration (Spikes + high noise)
faulty = np.sin(2 * np.pi * 50 * t) + np.random.normal(0, 0.8, 1000)
# Adding "Shocks" or spikes which happen in bearing cracks
faulty[::50] += 2.5 

# 3. Create a DataFrame
df_healthy = pd.DataFrame({'vibration': healthy, 'label': 'Healthy'})
df_faulty = pd.DataFrame({'vibration': faulty, 'label': 'Faulty'})

# Combine and Save
df = pd.concat([df_healthy, df_faulty])
df.to_csv('machine_data.csv', index=False)

print("✅ Success: 'machine_data.csv' generate ho gayi hai. Storage use: < 1MB!")

# 4. Visualize (Taaki tu dekh sake ki farq kya hai)
plt.figure(figsize=(12, 5))
plt.plot(healthy[:200], label="Healthy (Normal Operation)", color='green')
plt.plot(faulty[:200], label="Faulty (Bearing Crack)", color='red', alpha=0.7)
plt.legend()
plt.title("Mechanical Vibration Pattern: Healthy vs Faulty")
plt.show()