# Monte Carlo Simulation of Muon Lifetimes

## Overview

In the previous parts of this project, I used mathematical formulas to calculate how the number of surviving muons changes over time.

In this section, I wanted to take a different approach and simulate individual muons instead of only looking at the average behaviour.

To do this, I used a Monte Carlo simulation.

---

## What is a Monte Carlo Simulation?

A Monte Carlo simulation is a method that uses random numbers to model real-world processes.

Instead of assuming that every muon behaves exactly the same way, I generate a random lifetime for each muon.

Some muons decay very quickly, while others survive longer.

When thousands of muons are simulated, the overall pattern matches the exponential decay law studied earlier.

---

## Objective

The goal of this program is to:

* Simulate 10,000 individual muons
* Generate random lifetimes
* Visualize the distribution of those lifetimes
* Compare the simulation with the expected physical behaviour

---

## How the Simulation Works

The simulation uses NumPy's exponential distribution function.

Each muon receives a random lifetime based on the known mean lifetime of a muon:

2.2 × 10⁻⁶ seconds

The generated lifetimes are then displayed in a histogram.

---

## Technologies Used

* Python
* NumPy
* Matplotlib

---

## Output

The program produces a histogram showing the simulated lifetimes.

The histogram shows that:

* Most muons decay shortly after being created.
* Fewer muons survive for longer periods.
* Very long-lived muons are rare.

This matches the expected behaviour of exponential decay.

---

## What I Learned

While working on this section, I learned:

* How Monte Carlo simulations work
* How randomness can be used to model physical systems
* The difference between a theoretical model and a simulation
* How probability distributions appear in particle physics

---

## Next Step (UPDATED LATER)

In the next part of the project, I will use these simulated lifetimes to investigate how many muons can survive the journey from the upper atmosphere to Earth's surface.
