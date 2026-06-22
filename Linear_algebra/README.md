# Linear Algebra Formulation of Muon Decay

## Why I Added This Section

Up to this point, the project used physics formulas, probability distributions and simulations to study muon decay.

I wanted to explore whether the same process could also be described using linear algebra.

This section was my introduction to using vectors and matrices to model a physical system.

---

## The Main Idea

Instead of tracking only the total number of muons, I represent the system as a state vector.

The vector keeps track of:

* Alive muons
* Decayed muons

At each step, a transition matrix determines how the system changes.

By repeatedly multiplying the matrix by the state vector, the decay process can be simulated over time.

---

## Why This Is Interesting

One thing I found interesting is that the transition matrix is not arbitrary.

The survival probability inside the matrix comes directly from the same exponential decay law used earlier in the project.

This means the linear algebra model and the physics model describe the same process in different ways.

---

## Matrix Powers

I also explored matrix powers.

Instead of applying the transition matrix repeatedly, it is possible to compute:

A¹⁰⁰

and jump directly to the final state.

This produced the same result while requiring fewer calculations.

---

## Relativity and Matrices

Another reason I wanted to include linear algebra is that Special Relativity itself uses matrices.

Lorentz transformations can be represented as matrix operations that transform spacetime coordinates between different reference frames.

I included a simple example to see how an event appears from another frame of reference.

---

## Tools Used

* Python
* NumPy
* Matplotlib

---

## Concepts Used

### Physics

* Muon decay
* Time dilation
* Lorentz transformations

### Mathematics

* Vectors
* Matrices
* Matrix multiplication
* Matrix powers

---

## What I Learned

This section helped me understand that linear algebra is much more than a collection of abstract mathematical rules.

It can be used to describe how physical systems evolve and how different reference frames are related.

It was interesting to see how the same muon decay process could be represented using both exponential functions and matrix operations.

---

## Final Reflection

This project started with a simple exponential decay equation and gradually expanded into relativity, probability, simulation and linear algebra.

Working through each stage helped me understand how different areas of mathematics and physics connect to one another when studying a real phenomenon.
