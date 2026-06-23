# Exponential Decay of Muons

## Why I Started This Project

I have always found it interesting that tiny particles created high in Earth's atmosphere can still be detected at ground level.

While reading about muons, I learned that they only live for about 2.2 microseconds on average. That immediately raised a question for me:

**If muons live for such a short time, how are so many of them able to survive long enough to reach Earth?**

To start exploring that question, I first needed to understand how muons decay over time.

---

## What This Program Does

In this first part of the project, I model the decay of muons using the exponential decay equation.

I start with 10,000 muons and calculate how many remain as time passes.

The result is displayed as a graph showing the decrease in the number of surviving muons.

---

## The Physics Behind It

Muons are unstable particles, which means they naturally decay after a certain amount of time.

Their average lifetime is:

**2.2 microseconds (2.2 × 10⁻⁶ seconds)**

The number of surviving muons follows the exponential decay law:

N(t) = N₀ × e^(-t/τ)

where:

* N(t) is the number of surviving muons
* N₀ is the initial number of muons
* τ is the average lifetime
* t is the elapsed time

---

## Tools Used

* Python
* NumPy
* Matplotlib

---

## Program Settings

| Parameter               | Value            |
| ----------------------- | ---------------- |
| Initial number of muons | 10,000           |
| Muon lifetime           | 2.2 × 10⁻⁶ s     |
| Time interval           | 0 to 10 × 10⁻⁶ s |

---

## Output

The program generates a graph showing how the number of surviving muons decreases over time.

As expected, the curve drops rapidly because more and more muons decay as time passes.

---

## What I Learned

While working on this part of the project, I learned:

* How exponential decay is used to model unstable particles
* How to perform scientific calculations with NumPy
* How to visualize physical processes using Matplotlib
* How a simple mathematical equation can describe a real physical phenomenon

---

## Looking Ahead (UPDATED LATER)

This model assumes that muons are stationary.

In reality, many muons travel at speeds very close to the speed of light.

In the next section, I will explore how Einstein's Special Relativity changes the picture and helps explain why muons are still observed at Earth's surface.
