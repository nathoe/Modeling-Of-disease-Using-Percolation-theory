# Python Code for description of a percolation model of disease propagation
import  numpy  as np
import itertools
from collections import Counter
import matplotlib.pyplot as plt
N = 130 # population is N*N
x = 0.4# proportion of immunised
t =0.3 #t is the probability tha the person transmit the disease after getting infected
n_last = -1 
n = 0
duration =150
P = np.zeros([N+1,N+1],float)
size = np.zeros(N+1)
minp = np.zeros(N+1,dtype=int )
maxp = np.zeros(N+1,dtype=int)
ni = np.zeros(duration,int)
g = np.zeros(duration,int)
pi = np.zeros(duration,int)


for i in range(N+1):
     minp[i] = int(i-1)
     maxp[i] = int(i+1)
minp[0] = 0
maxp[N] = N
b = np.linspace(0,duration,duration)#the array for the number of days
        
for i in range(len(size)):
     for j in range(len(size)):
         r = np.random.randn()  # immunize a fraction 'x' of population
         if r< x:
             P[i,j] = 0 # immunize
         else:
             P[i,j] = 1  # leave uninfected

P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3# infect the first individual manually
plt.imshow(P,origin="lower")
totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
print ("The number of new infected people at the origin is:",totals[3],\
      "The number of immunized people after origin is:",totals[0],\
      "The number of uninfected people at the origin is:",totals[1])
plt.show()             
#  keep going until as many people  are infected
for day in range(duration):
     for i in range(len(size)):
          for j in range(len(size)):
               if (P[i,j] ==3):
                    # if infected, then infect the neighbors
                    n=n+1 # count how many infected
                    if (P[minp[i],j]==1):
                         if t >= np.random.randn():      
                              P[minp[i],j]=2
                         else:
                              P[minp[i],j]==1
                    if (P[maxp[i],j]==1):
                         if t >= np.random.randn():
                              P[maxp[i],j]=2
                         else:
                              P[maxp[i],j]==1
                    if (P[i,minp[j]]==1):
                         if t>= np.random.randn():
                              P[i,minp[j]]=2
                         else:
                              P[i,minp[j]]==1
                    if (P[i,maxp[j]]==1):
                         if t>=np.random.randn():
                              P[i,maxp[j]]=2
                         else:
                              P[i,maxp[j]]==1
                    if (P[minp[i],minp[j]]==1):
                         if t>=np.random.randn():
                              P[minp[i],minp[j]]=2
                         else:
                              P[minp[i],minp[j]]==1
                    if (P[maxp[i],maxp[j]]==1):
                         if t >= np.random.randn():
                              P[maxp[i],maxp[j]]=2
                         else:
                              P[maxp[i],maxp[j]]==1
                    if (P[maxp[i],minp[j]]==1):
                         if t >= np.random.randn():
                              P[maxp[i],minp[j]]=2
                         else:
                              P[maxp[i],minp[j]]==1
                    if (P[minp[i],maxp[j]]==1):
                         if t>=np.random.randn():
                              P[minp[i],maxp[j]]=2
                         else:
                              P[minp[i],maxp[j]]==1                          
     for i in range(len(size)):
          for j in range(len(size)):
               if (P[i,j] ==2):
                    P[i,j]= 3
     #if day == 5:
      #    P[N*rand(),N*rand()] = 3 #after 20 days infected person jump to another village
     if day == 10:
          P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3



     if (day == duration/8):
          plt.imshow(P,origin="lower")
          plt.title("22 days")
          totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
          print ("The number of new infected people after",duration/8," days is:",totals[3],\
                "The number of uninfected people is:",totals[1])
          plt.show()
     if day == 40:
          P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3 #after 40 days infected person jump to another village


     if (day == duration/4):
          plt.imshow(P,origin="lower")
          plt.title('45 days')
          totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
          print ("The number of new infected people after ",duration/4," days is:",totals[3],\
                "The number of uninfected people is:",totals[1])
     if day == 60:
          P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3 #after 60 days infected person jump to another village

     if day == 80:
          P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3#jump after day 80

          plt.show()
     if (day == duration/2):
          plt.imshow(P,origin="lower")
          plt.title('90 days')
          totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
          print ("The number of new infected people after",duration/2," days is:",totals[3],\
                "The number of uninfected people is:",totals[1])
          plt.show()
     if day == 100:
          P[np.random.choice(N,1).item(),np.random.choice(N,1).item()] = 3 #after 100 days infected person jump to another village


     totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
     ni[day] = totals[3]-totals[2] # number of new infection daily
     pi[day] = totals[3]


plt.imshow(P,origin="lower")
plt.title('last day')
plt.show()
totals = Counter(i for i in list(itertools.chain.from_iterable(P)))
print ("The number of new infected people in last day is:",totals[3],\
     "The number of uninfected people is:",totals[1])
for q in range(1,duration):
     g[q-1]=ni[q]-ni[q-1]
print ("The immunization rate ",x,", and the transmition rate is ",t)
plt.plot(b,g)#number of new infection per day
plt.xlabel('the number of days')
plt.ylabel('number infected people per day')
plt.xlim(0,duration)
#ylim(0,N)
plt.show()
plt.plot(b,pi+48,label="cumulation vs time")
#data=np.loadtxt("values.txt",float)
#x=data[:,0]	
#z=data[:,1]
#plt.plot(x,z,"k.",label= "spread of ebola in Guinea")# the scatter graph of ebola spread in Guinea
plt.legend(loc='best')
plt.show()

                       
               
    


         
