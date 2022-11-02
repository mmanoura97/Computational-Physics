""""Computational-Physics Python exercise

Consider a box which is divided into two equal parts, with a wall. There are nanoparticles in the box. The wall dividing the box has a hole which allows the nanoparticles to pass through. Every second only one nanoparticle passes through the hole. We assume that the set of nanoparticles N, are initially in one space of the box and the hole is closed. We open the hole and the nanoparticles come and go randomly until equilibrium is reached.

Statistically, the number of nanoparticles in one part (a) of the box in as a function of time is given by the equation:

Na = (N / 2) * (1 + exp(-2 * t / N))

Simulate the problem with python code, and present a diagram of the nanoparticles as a function of time. The total simulation time is 100,000 s.In the same diagram represent the above theoretical relationship. Run the simulation for a total number of nanoparticles N = 1000, and record through your code the time it takes your computer's CPU to run the simulation. """"