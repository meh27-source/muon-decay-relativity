# Muon Survival Simulation

## Why I Made This

After learning that a muon only lives for about 2.2 microseconds, I started wondering how scientists are able to detect so many muons at Earth's surface.

If muons are created high in the atmosphere, shouldn't most of them decay before reaching the ground?

This section of the project is my attempt to investigate that question using a simulation.

---

## The Idea

I assumed that muons are created about 15 km above Earth and travel towards the surface at a speed very close to the speed of light.

Using the random lifetimes generated in the previous section, I checked whether each simulated muon survives long enough to complete the journey.

If a muon's lifetime is longer than the travel time, it is counted as a survivor.

---

## What I Wanted to Compare

I ran the simulation twice:

### Scenario 1

Using the normal muon lifetime:

* 2.2 microseconds

### Scenario 2

Using the lifetime predicted by Special Relativity:

* time dilation included

This allowed me to compare how much of a difference relativity actually makes.

---

## How the Simulation Works

1. Calculate the travel time from the atmosphere to Earth.
2. Generate random muon lifetimes.
3. Compare each lifetime with the travel time.
4. Count the surviving muons.
5. Repeat the process with relativistic time dilation.

---

## Tools Used

* Python
* NumPy
* Matplotlib

---

## Results

The simulation clearly shows that many more muons survive when relativistic effects are included.

Without time dilation, only a small fraction of muons reach Earth's surface.

With time dilation, the number of surviving muons increases dramatically.

This helped me understand why muons are routinely detected on Earth despite their short lifetime.

---

## What I Learned

This was probably the most interesting part of the project so far because it connected the theory directly to a real observation.

While working on this section, I learned:

* How simulations can be used to answer physics questions
* Why Special Relativity is necessary in particle physics
* How random sampling can model large groups of particles
* How a seemingly small change in lifetime can have a huge effect on the final result

---

## Next Step (UPDATED LATER)

In the final part of the project, I will explore how the same system can be described using vectors, matrices and linear algebra.
