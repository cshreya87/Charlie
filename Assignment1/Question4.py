#Group Name : Charlie
#Rinku Chowdhury : 216101118
#M.Rauf Qureshi : 216100729
#Shreya Chatterjee : 216100848

import matplotlib.pyplot as plt
import numpy as np
import random as rn
x=set()
for m in range(0,10):
	x.add(rn.randint(0,90))
x=sorted(x)
m=list(x)

ySin = np.sin(m) 
yCos = np.cos(m)

#Set title and plot the graph, set red color for Sin and Blue for Cos
plt.title('Sin and Cos functions')
plt.plot(x, ySin,'r' ,x,yCos,'b')

# Get plot axis and change y axis limits 
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,-2,2))

#Add labels, legend and show the graph
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.legend(['Sine', 'Cosine'])
plt.show()