---
layout: post
title: "Spin"
date: 2026-01-05
---

This chapter develops some important ideas that were introduced last blog - Measuring in different directions.

### Mathematics

First we need to define how we are going to represent spin. We are going to create the mathematical "environment" that will represent spin. 

The basic model is using vectors, as introduced in the last blog. The dimension of the vector space depends on the number of possible outcomes. For spin, we only have 2 outcomes - N or S. Choosing a direction to measure spin, then, means to choose an ordered, orthonormal basis (|b1>, |b2>). This means these 2 vectors correspond to our possible outcomes (N or S).

This idea didn't click with me at first. Again, we are just making an environment which we can use to describe the behavior of spin. 

![image](/assets\images\qml\image1.png)

This means we are going to associate spin N with the basis in the y direction, and spin S with the basis in the x direction. Now, we are going to change this notation a bit:

- Spin Up |↑⟩ = [1, 0]ᵀ = electron having spin N in direction 0 degrees 
- Spin Down|↓⟩ = [0, 1]ᵀ = electron having spin S in direction 0 degrees 

We define direction 0 degrees as the direction towards 12 on a clock. This does NOT mean, physical direction [1, 0]ᵀ. [1, 0]ᵀ is not a direction of spin, but rather how we represent the state of the spin. The vector [1, 0]ᵀ tells us the electron is in the |↑⟩ state (100% probability of measuring spin N), while the physical spin direction is 0 degrees (north on our clock).

So, how would we represent any state in between up and down? remember, spin can be in a *combination* of those 2 states. The spin will be in a linear combination of |b1> and |b2>, which is represented as c1|b1> + c2|b2>. This is called the *state vector* because it represents the current state of the spin. 

So just to recap, before we measure the spin of the electron, it will be in some state in between the 2 basis, so it is in state c1|b1> + c2|b2>. Once we make a masurement, it will go to either |b1> or |b2>. To represent this mathematically let's say |b1> is up and |b2> is down. We measure the spin, and get that it is Up. We then get the following state: 1|b1> + 0|b2>. This means the spin has 100% *probability* to be in state b1 (up), and 0% probability in state b2 (down). Therefore, c can be thought of as the probability of the state vector being in some basis. It is called the *probability amplitude*. In reality, we have to square this value to get the actual probability, but we'll explain that later. 

So, what happens when we measure spin in the horizontal directions?


