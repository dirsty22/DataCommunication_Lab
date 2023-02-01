import numpy as np
import matplotlib.pyplot as plt

figure,axis=plt.subplots(3)
plt.tight_layout()
#carrier signal
x=list(np.arange(0,5,0.01))
x.append(x[-1]+0.01)
A= 5
f= 2
phase= 0
x= np.array(x)

y = A*np.cos(2*np.pi*f*x+phase)
axis[0].grid(True)
axis[0].plot(x,y,color='blue')
axis[0].set_title('Carrier Signal')

#Message signal
sig_f = 0.2
y1 = A*(np.sin(2*np.pi*sig_f*x+phase))
axis[1].grid(True)
axis[1].plot(x,y1,color='red')
axis[1].set_title('Message Signal')

#PM Signal
y2 = A*np.cos(2*np.pi*(f+y1)+phase)
axis[2].grid(True)
axis[2].plot(x,y2,color='red')
axis[2].set_title('PM signal')
plt.show()

