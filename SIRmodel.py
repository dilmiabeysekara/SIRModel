#Author Chandima Dilmi Abeysekara
#Homework #3


import matplotlib.pyplot as plt

#Define lists to save time dependent variables
s = []          #Number of susceptible individuals
Ia = []         #Number of infected individuals
t = []          #Time

dt = 1          #The time gap for simulations

v = 0.5         #Survival rate
N = 1000000     #Total number people within the community
alpha = 15./100.#Probability to die
I0 = 1000       #Initial number of infected individuals
s0 = N-I0       #Initial number of susceptible individuals
g= 1./5.        #Probability of recovered individuals join the susceptible population,
beta = 6.30630630631e-07 #Probability to transfer the disease

s.append(s0)
Ia.append(I0)
t.append(0)


for i in range (1,500):
         t.append(i*dt)
         s.append(s[i-1] + (-1*beta*s[i-1]*Ia[i-1] + v*g*Ia[i-1])*(t[i] - t[i-1]))
         Ia.append(Ia[i-1] +(beta*s[i-1]*Ia[i-1] - v*Ia[i-1] - alpha*Ia[i-1])*(t[i]- t[i-1]))

plt.figure(1)
plt.ylim([950000,1000000])
plt.plot(t,s,'g-',label='s')
plt.xlabel('Time')
plt.ylabel('Susceptible Population')

plt.figure(2)
plt.ylim([0,1000])
plt.plot(t,Ia,'r-',label='I')
plt.xlabel('Time')
plt.ylabel('Infected Population')

plt.show()
