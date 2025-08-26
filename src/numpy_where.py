import numpy as np
a = np.array([1,2,3,10,20,30,0.1,0.2])
print(a)
print(np.min(a),np.max(a))
print(np.where(a<1))            # showing index where a <1  
print(np.where(a < 5, a, 10*a)) # showing index where if a <5 , put a otherwise a <- conditional index = 10 * a

