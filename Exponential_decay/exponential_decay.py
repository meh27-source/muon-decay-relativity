import numpy as np
import matplotlib.pyplot as plt

MUON_LIFETIME = 2.2e-6
N0 = 10000

t = np.linspace(0, 10e-6, 1000)

N = N0 * np.exp(-t / MUON_LIFETIME)

plt.figure(figsize=(8, 5))
plt.plot(t, N)
plt.title("Muon Exponential Decay")
plt.xlabel("Time (s)")
plt.ylabel("Surviving Muons")
plt.grid(True)
plt.show()

# Notes
#
# Muons are unstable particles.
#
# Their decay follows an exponential law:
#
# N(t) = N0 * exp(-t/tau)
#
# N0  = initial number of muons
# tau = mean lifetime
# t   = time
#
# This model shows how the number of
# surviving muons decreases over time.