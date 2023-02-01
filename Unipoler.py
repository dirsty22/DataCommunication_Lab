import numpy as np
import matplotlib.pyplot as plt
data=[0,1,0,1,1]
plt.title('Unipolar Representation :')
time=np.arange(0,len(data),1)
plt.step(time,data,where='post')
plt.show()
