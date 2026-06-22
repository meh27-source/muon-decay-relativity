# Exponential Decay of Muons

## Overview

This is the first stage of the Muon Decay and Special Relativity project.

The objective of this section is to model the decay of muons over time using Python and visualize the resulting exponential decay curve.

---

## Physics Background

Muons are unstable elementary particles produced in the upper atmosphere when cosmic rays collide with atoms.

A muon does not live forever. Instead, it decays after a short period of time.

The average lifetime of a muon is approximately:

**2.2 microseconds (2.2 × 10⁻⁶ seconds)**

The number of surviving muons decreases according to the exponential decay law:

N(t) = N₀ × e^(-t/τ)

where:

* N(t) = number of surviving muons at time t
* N₀ = initial number of muons
* τ = mean lifetime of the muon
* t = elapsed time

---

## Objective

The goal of this program is to:

* Simulate the decay of 10,000 muons
* Apply the exponential decay equation
* Visualize how the number of surviving muons changes over time

---

## Technologies Used

* Python
* NumPy
* Matplotlib

---

## Mathematical Concepts

This project uses:

* Exponential functions
* Scientific notation
* Numerical computation
* Data visualization

---

## Program Parameters

| Parameter           | Value            |
| ------------------- | ---------------- |
| Initial muons (N₀)  | 10,000           |
| Muon lifetime (τ)   | 2.2 × 10⁻⁶ s     |
| Simulation interval | 0 to 10 × 10⁻⁶ s |

---

## Output

The program generates a graph showing:

* Time on the x-axis
* Number of surviving muons on the y-axis

The curve decreases exponentially because more and more muons decay as time passes.

---

## What I Learned

Through this project I learned:

* How exponential decay models particle lifetimes
* How to perform scientific calculations using NumPy
* How to create graphs using Matplotlib
* How physical processes can be represented computationally

---

## Next Step (UPDATED LATER)

In the next section, Special Relativity will be introduced to investigate why many muons are still able to reach Earth's surface despite their short lifetime.
