import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
color = 'tab:red'
ax.plot([1,2,3,4],[1,4,2,3], color = color)
ax.set_xlabel('nodes')
ax.set_ylabel('time (s)',color = color)
ax.set_title('Simulator')
ax2 = ax.twinx()
color = 'tab:blue'
ax2.set_ylabel('Efficiency',color = color)
ax2.plot([1,2,3,4],[2,1,3,4], color = color)
plt.show()