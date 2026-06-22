import numpy as np
import matplotlib.pyplot as plt

muon_lifetime = 2.2e-6
number_of_muons = 10000

c = 3e8
v = 0.998 * c

gamma = 1 / np.sqrt(1 - (v**2 / c**2))
dilated_lifetime = gamma * muon_lifetime

height = 15000

travel_time = height / v

lifetimes = np.random.exponential(
    muon_lifetime,
    number_of_muons
)

survivors_without_relativity = np.sum(
    lifetimes > travel_time
)

lifetimes_rel = np.random.exponential(
    dilated_lifetime,
    number_of_muons
)

survivors_with_relativity = np.sum(
    lifetimes_rel > travel_time
)

print(f"Travel time: {travel_time:.2e} s")
print(f"Gamma factor: {gamma:.2f}")

print(
    f"Survivors without relativity: "
    f"{survivors_without_relativity}"
)

print(
    f"Survivors with relativity: "
    f"{survivors_with_relativity}"
)

plt.figure(figsize=(8, 5))

plt.bar(
    ["Without Relativity", "With Relativity"],
    [survivors_without_relativity,
     survivors_with_relativity]
)

plt.title("Muon Survival to Earth's Surface")
plt.ylabel("Number of Surviving Muons")
plt.grid(axis="y")

plt.show()

# Notes
# Muons are assumed to be created
# about 15 km above Earth.
# The travel time is calculated using: time = distance / speed
# A muon survives if its lifetime is greater than the travel time.
# Relativity increases the lifetime and therefore increases the numberof surviving muons.