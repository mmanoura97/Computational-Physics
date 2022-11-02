import random
import matplotlib.pyplot as plt
import numpy as np
import time



#get the start time
st = time.process_time()

#N = total number of nanoparticles
N = 1000

#for t = 0 
Na = N #Number of nanoparticles in box A
Nb = 0 #Number of nanoparticles in box B
 
t = 0 #At first t = 0
list = [Na, Nb, 0] #i am making a list to keep the coordinates i will use on the plot
 
#Simulating the process in 100000sec duration
for i in range(1,100000):
 if Na != Nb: #if Na = Nb we have thermodynamic equilibrium and the process stops
  r = random.randint(1,N) #i randomly choose a particle
  if r <= Na: #I am checking if the random particle i picked is on box A 
   Na = Na - 1 #the random particle i picked is getting out of box A
   Nb = Nb + 1 #the random particle i picked is getting in box B
  else: #the random particle i picked is on box B
   Na = Na + 1 #the random particle i picked is getting in box A
   Nb = Nb - 1 #the random particle i picked is getting out of box B
  list = list + [Na, Nb, i] #this way i have each second the particles on each box
 else:
  break

#making the plot
x = [] #the points of x-axis (time)
ya = [] #the point of y-axis for box A - numbers of particles on box A
yb = [] #the point of y-axis for box B - numbers of particles on box B
 
for i in list:
 x = list[2::3] #i am keeping the seconds of the process
 ya = list[::3] #i am keeping the numbers of particles on box A
 yb = list[1::3] #i am keeping the numbers of particles on box B

plt.plot(x, ya, label = 'line Na')
plt.plot(x, yb, label = 'line Nb')
plt.xlabel('Time (sec)')
plt.ylabel('Number of Particles in Box A (Na)')

#now i want to make the plots using the existing formula Na = N/2*(1 + exp**(-2*t)/N)
formula = np.divide(x, N)
formula = (-2) * formula
formula = np.exp(formula)
formula = formula + 1
formula = formula * N
formula = formula / 2
plt.plot(x, formula, label = 'line Na using formula')
leg = plt.legend(loc='upper right')

plt.show()

#get the end time
et = time.process_time()

#get execution time
res = et - st

print('CPU Execution time:', res, 'seconds')

