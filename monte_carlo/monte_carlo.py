import numpy as np
import matplotlib.pyplot as plt

muon_lifetime = 2.2e-6
number_of_muons = 10000

lifetimes = np.random.exponential(
    muon_lifetime,
    number_of_muons
)

average_lifetime = np.mean(lifetimes)

print(f"Average simulated lifetime: {average_lifetime:.2e} s")

plt.figure(figsize=(8, 5))

plt.hist(
    lifetimes,
    bins=50,
    edgecolor="black"
)

plt.title("Simulated Muon Lifetimes")
plt.xlabel("Lifetime (s)")
plt.ylabel("Number of Muons")
plt.grid(True)

plt.show()

# Notes
# Every muon is assigned a random lifetime.
# The lifetimes are generated from an
# exponential distribution because muon
# decay follows an exponential law.
# Most muons decay quickly while only a
# small number survive for a long time.
# As the number of simulated muons
# increases, the distribution approaches
# the theoretical decay model.