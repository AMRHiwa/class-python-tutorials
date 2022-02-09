"""import matplotlib
import matplotlib.pyplot as plt
import numpy as np

p = np.arange(1,20)
print(p)

plt.plot(p)      #make the chart
plt.show()       #show the chart

--------------------------------------------------------

import matplotlib
import matplotlib.pyplot as plt
# import numpy as np

plt.plot([5, 6, 11], "purple")      #make the chart
plt.show()       #show the chart

---------------------------------------------------------

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,21)       #make a array from 1 to 20
y = x ** 2                #make a array wit x**2

plt.plot(x , y)           #make a chart with x, y
plt.xlabel("x")           #create a label for x
plt.ylabel("f(x) = X^2")  #create a label for y
plt.title("the chart!")   #create a title for chart

plt.show()                #show a chart
---------------------------------------------------------

import matplotlib
import matplotlib.pyplot as plt

x1 = ["Farvardin", "Ordibehesht", "Khordad"]
x2 = [10, 20, 30]                           # must len(x1) = len(x2)

y1 = ["Math", "Chemestri", "Programming"]
y2 = [40, 50, 20]                           # must len(y1) = len(y2)

plt.plot(x1, y1)

plt.xticks(x2, x1)                          # We attribute x1 to x2
plt.yticks(y2, y1)                          # We attribute y1 to y2

plt.show()
---------------------------------------------------------
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10, 0.01) # make a array for time (sec)
y = np.sin(2*np.pi*t)   # use sin function from numpy

plt.plot(t, y)         #  create a chart for sin
plt.xlabel("time")     # label for x
plt.ylabel("output")   # label for y
plt.title("Sin")       # title for this chart
plt.show()             # show the chart