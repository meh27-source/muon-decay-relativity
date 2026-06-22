import numpy as np
import matplotlib.pyplot as plt

MUON_LIFETIME = 2.2e-6
N0 = 10000

c = 3e8
v = 0.998 * c

gamma = 1 / np.sqrt(1 - (v**2 / c**2))

dilated_lifetime = gamma * MUON_LIFETIME

t = np.linspace(0, 10e-6, 1000)

N = N0 * np.exp(-t / MUON_LIFETIME)
N_rel = N0 * np.exp(-t / dilated_lifetime)

plt.figure(figsize=(8, 5))
plt.plot(t, N, label="Without Relativity")
plt.plot(t, N_rel, label="With Relativity")
plt.title("Muon Decay with Time Dilation")
plt.xlabel("Time (s)")
plt.ylabel("Surviving Muons")
plt.legend()
plt.grid(True)
plt.show()

print(f"Gamma factor: {gamma:.2f}")
print(f"Dilated lifetime: {dilated_lifetime:.2e} s")

# Notes

# Muons travel close to the speed of light.
# According to Special Relativity,
# moving clocks run slower.
# Gamma factor: gamma = 1 / sqrt(1 - v²/c²)
# Time dilation:tau' = gamma * tau
# Fast-moving muons therefore appear
# to live longer from Earth's frame.