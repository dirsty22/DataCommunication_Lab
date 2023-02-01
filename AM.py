import numpy as np
import matplotlib.pyplot as plt

figure,axis=plt.subplots(3)
#carrier signal
x=list(np.arange(0,5,0.01))
x.append(x[-1]+0.01)
A= 5
f=5
phase= np.pi/2
x= np.array(x)

y = A*np.sin(2*np.pi*f*x+phase)
axis[0].grid(True)
axis[0].plot(x,y,color='blue')
axis[0].set_title('Carrier Signal')

#Message signal
sig_f = 1
y1 = ((np.sin(2*np.pi*sig_f*x+phase)) + (np.cos(2*np.pi*sig_f*x+phase)))
axis[1].grid(True)
axis[1].plot(x,y1,color='red')
axis[1].set_title('Send Signal')

#AM Signal
y2 = y + y1
axis[2].grid(True)
axis[2].plot(x,y2,color='red')
axis[2].set_title('AM')
plt.show()
