import matplotlib.pyplot as plt
import numpy as np

f,(ax1,ax2)=plt.subplots(1,2)

#plot1
x1=np.array([1,3,5,7,10])
y1=np.array([3,8,1,10,4])
ax1.plot(x1,y1)

#plot2
x2=np.array([-10,-15,8,4,20])
y2=np.array([-1,-3,5,7,9])
ax2.plot(x2,y2)

plt.show()
