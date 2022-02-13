
# many example for matplotlib packeg and make chart in python

# -------------- example #1 --------------

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

p = np.arange(1,20)
print(p)

plt.plot(p)      #make the chart
plt.show()       #show the chart

# -------------- example #2 --------------
import matplotlib
import matplotlib.pyplot as plt
# import numpy as np

plt.plot([5, 6, 11], "purple")      #make the chart
plt.show()       #show the chart

# -------------- example #3 --------------

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
# -------------- example #4 --------------

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
# -------------- example #5 ---------------

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

# -------------- example #6 ----------------

import numpy as np
import matplotlib.pyplot as plt

def f(t):                     # create a function to calcute a sin(2*Pi*t) * cos(2*Pi*t)
    return np.sin(2 * np.pi * t) * np.cos(2 * np.pi * t)

t1 = np.arange(0, 10, 0.01)   # create a range for time (t1)
t2 = np.arange(2, 12, 0.01)   # create a range for time (t2)
plt.plot(t1, f(t1), "bo", t2, f(t2), "r")  # create a chart for both of time's ranges and formula
plt.xlabel("time (sec)")      # associate a name for the community x
plt.ylabel("output")          # associate a name for the community y
plt.title("sin(2Pit) * cos(2Pit)")         # associate a name for the chart
plt.show()                    # show the chart

# -------------- example #7 --------------

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20)     # create the range from 0 to 20
plt.bar(x, x**3, align="center", width=0.5, color="red")  # create a bar chart for x and x^3
plt.show()           # show the chart

# -------------- example #8 ---------------

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20)   # create a range from 0 to 20
plt.scatter(x, x**3, linewidths=2, color="purple")   # create a scatter chart for x , x^3
plt.show()          # show the chart
# -------------- example #9 ---------------

import numpy as np
import matplotlib.pyplot as plt

# create a range from 0 to 20
x = np.arange(20)       

# create a scatter chart for x and x + random_value
plt.scatter(x, x + np.random.randn(len(x)), linewidths=1.5, color="purple")  

# show the chart 
plt.show()
# -------------- example #10 ----------------

import numpy as np
import matplotlib.pyplot as plt

# create a range from 0 to 20
x = np.arange(20)       

# create a step chart for x and x^3
plt.step(x, x**3, color="orange", linewidth=1.25)

# show the chart 
plt.show()
# -------------- example #11 ----------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

# create a set for lessons scores
score = [40, 60, 30, 90, 100, 55]

# create a set for lessons names
lesson = ["math", "physics", "geography",
          "data structure", "programming", "chemestry"]

# create a pie chart for lessons and scores with pylab form matplotlib
pl.pie(score, labels= lesson)

# show the chart
plt.show()
# -------------- example #12 ----------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

# create a set for lessons scores
scores = [np.random.randint(1, 100) for i in range(5)]

# create a set for lessons names
lesson = ["math", "physics", "geography",
          "data structure", "programming"]

# create a pie chart for lessons and scores with pylab form matplotlib
pl.pie(scores, labels= lesson)

# show the scores for user
for score in scores:
    print(score)

# show the chart
plt.show()
# -------------- example #13 ----------------

import numpy as np
import matplotlib.pyplot as plt

# make a set of 100 random value
data = np.random.randn(100)

# create a histogram chart 
plt.hist(data)

# associate a name for the community x
plt.xlabel("Data")

# associate a name for the chart
plt.title("Histogram")

# show the chart
plt.show()
# -------------- example #14 -----------------

import matplotlib.pyplot as plt
import matplotlib.pylab as pl

# make a sets from random value
data1 = pl.randn(300)
data2 = pl.randn(300)

# create a histogram chart for data1 and data2
plt.hist([data1, data2])

# show the chart 
plt.show()
# -------------- example #15 -------------------

import matplotlib.pyplot as plt
import pylab as pl

# make a sets from random value
data1 = pl.randn(500)
data2 = pl.randn(500)

# create a histogram chart for data1 and data2
plt.hist([data1, data2], label=["Data1", "Data2"])

# make guide for chart with it's labels
pl.legend()

# save a picture from chart in your system
plt.savefig("picture_name_and_address.jpg")

# show the chart 
plt.show()
# ---------------------------------------------------------
