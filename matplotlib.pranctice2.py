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
"""
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