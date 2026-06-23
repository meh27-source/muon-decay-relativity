# Relativistic Muon Decay

## Why I Added This Section

After creating the exponential decay model, I ran into an interesting problem.

Muons only live for about 2.2 microseconds on average. Based on the first simulation, it seemed unlikely that many of them should survive long enough to travel from the upper atmosphere to Earth's surface.

However, experiments show that muons are detected at ground level all the time.

This made me curious about what was missing from the simple decay model.

The answer turns out to be Einstein's Special Theory of Relativity.

---

## The Question

If muons decay so quickly, why are so many of them still observed on Earth?

To investigate this, I compared two situations:

* Muon decay without relativistic effects
* Muon decay with relativistic time dilation

---

## The Physics Behind It

Many muons travel extremely close to the speed of light.

According to Special Relativity, time passes more slowly for objects moving at very high speeds.

This effect is known as **time dilation**.

The amount of time dilation is determined by the Lorentz factor:

γ = 1 / √(1 − v²/c²)

where:

* v is the velocity of the muon
* c is the speed of light

Using this factor, the observed lifetime becomes:

τ' = γτ

This means that from Earth's point of view, a fast-moving muon appears to live much longer than 2.2 microseconds.

---

## What This Program Does

The program calculates:

1. The normal exponential decay curve
2. A second decay curve using the relativistically dilated lifetime

Both curves are displayed on the same graph so that the effect of time dilation can be seen directly.

---

## Tools Used

* Python
* NumPy
* Matplotlib

---

## Output

The graph shows two different decay curves.

The classical curve decreases rapidly, while the relativistic curve decreases much more slowly.

Seeing both curves together makes it easy to understand how relativity changes the behaviour of fast-moving particles.

---

## What I Learned

While working on this section, I learned:

* Why Special Relativity is necessary to explain real observations
* How time dilation affects particle lifetimes
* How the Lorentz factor is calculated
* How a change in lifetime affects the decay curve

One thing I found particularly interesting is that the underlying decay process remains the same. The only thing that changes is how time is measured.

---

## Looking Ahead (UPDATED LATER)

So far, the project has used mathematical equations to describe the average behaviour of muons.

In the next section, I will take a different approach by simulating thousands of individual muons and giving each one a random lifetime using a Monte Carlo simulation.
