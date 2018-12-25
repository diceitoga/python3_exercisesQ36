import pandas as pd
import json
import numpy as np
from pprint import pprint
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_file, show
from collections import Counter
#http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars

fg1 = figure(x_axis_label = "x_axis",y_axis_label = "y_axis")
x = [1,2,3,4]
y = [1,2,3,4]

fg1.circle(x,y)

output_file("sample1_bokeh.html")
show(fg1)