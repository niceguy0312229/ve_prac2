# reference 
# https://pinkwink.kr/1233



import numpy as np
#import matplotlib.pyplot as plt
#matplotlib inline

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


t = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(t)

plt.figure(figsize=(12,6))
plt.figure(1)
plt.plot(t, y1)



def derivative(f, a, h=0.01):
    return (f(a + h) - f(a))/h

dy1dx = derivative(np.sin, t)

y1_d = np.r_[0,np.diff(y1)]/0.1    # when used diff function 


#plt.figure(2)
#plt.figure(figsize=(12,5))
plt.plot(t, dy1dx, 'r.', label='Calculated Difference')
plt.plot(t, np.cos(t), 'b', label='True Value (Cos function)')
plt.plot(t, y1, 'k', label='Original Value')
plt.plot(t, y1_d, 'y', label='Diff function used')
plt.legend(loc='best')
plt.show() 
plt.close('all')




