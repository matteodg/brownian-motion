import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
steps = 5000
random.seed(42)
x,y = np.cumsum(np.random.randn(steps)), np.cumsum(np.random.randn(steps))
points = 10
ip = lambda x, steps, points: np.interp(np.arange(steps*points), 
                                        np.arange(steps)*points, 
                                        x)
X, Y = ip(x, steps, points), ip(y, steps, points)
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_title('Brownian Motion')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(X, Y, color='blue',
        marker='o',  markersize=1)
