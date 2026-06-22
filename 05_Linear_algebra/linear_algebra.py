import numpy as np
import matplotlib.pyplot as plt

muon_lifetime = 2.2e-6
number_of_muons = 10000

state = np.array([
    number_of_muons,
    0
], dtype=float)

dt = 0.1e-6

survival_probability = np.exp(
    -dt / muon_lifetime
)

transition_matrix = np.array([
    [survival_probability, 0.0],
    [1 - survival_probability, 1.0]
])

alive_history = []
decayed_history = []

for _ in range(100):
    alive_history.append(state[0])
    decayed_history.append(state[1])
    state = transition_matrix @ state

plt.figure(figsize=(8, 5))

plt.plot(alive_history, label="Alive")
plt.plot(decayed_history, label="Decayed")

plt.title("Muon Decay Using Linear Algebra")
plt.xlabel("Time Step")
plt.ylabel("Number of Muons")
plt.legend()
plt.grid(True)

plt.show()

initial_state = np.array([
    number_of_muons,
    0
], dtype=float)

matrix_power = np.linalg.matrix_power(
    transition_matrix,
    100
)

final_state = matrix_power @ initial_state

print("Transition Matrix:")
print(transition_matrix)

print("\nState After 100 Steps:")
print(state)

print("\nState Using Matrix Power:")
print(final_state)

c = 3e8
v = 0.998 * c

beta = v / c

gamma = 1 / np.sqrt(
    1 - beta**2
)

lorentz_matrix = np.array([
    [gamma, -gamma * beta],
    [-gamma * beta, gamma]
])

event = np.array([
    c * 10e-6,
    2000
])

transformed_event = (
    lorentz_matrix @ event
)

print("\nOriginal Event:")
print(event)

print("\nTransformed Event:")
print(transformed_event)

# Notes
# State vector:[alive muons, decayed muons]
# Matrix multiplication evolves the system through time.
# Matrix powers allow many
# evolution steps to be computed
# at once.
#
# Lorentz transformations can
# also be represented using
# matrices.