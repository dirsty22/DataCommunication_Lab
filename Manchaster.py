import numpy as np
import matplotlib.pyplot as plt


figure,axis=plt.subplots(2)
def getSignal(bits):
    y = list()
    for bit in  bits:
        if bit is '1':
            y.append(-1)
            y.append(1)
        else:
                y.append(1)
                y.append(-1)
    return y

while True:
    inp = input('Enter your digital signal :')
    if(inp is ''):
       break
    y = list()
    for ch in inp:
       if ch is '0':
            y.append(0) 
       else:
           y.append(1) 

    x = np.arange(0,len(inp),1)
    print('y is :',y)
    axis[0].step
    sig=getSignal(inp)
    axis[1].grid(True)
    x=np.arange(0,len(sig))
    axis[1].step(x,sig,color='red',where='post')
    axis[1].set_title("Manchaster")
    plt.show()
    
