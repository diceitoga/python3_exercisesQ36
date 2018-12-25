'''
Ex 36 Plotting....Last exercise!! 
 Birthday Plots
Exercise 36 (and Solution)

This exercise is Part 4 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
Because it would take a long time for you to input the months of various scientists, 
you can use my scientist birthday JSON file. Just parse out the months
(if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

If you are using a purely web-based interface for coding, 
this exercise won’t work for you, since it requires installing the bokeh Python package. 
Now might be a good time to install Python on your own computer.

Discussion

Today’s topic is going to be about the bokeh plotting library. 
We create plots and charts to display and communicate information from data, 
and it would be great to do that directly from Python. 
Sometimes it is really nice to write code or algorithms from scratch to learn and practice, 
and sometimes, someone has already written the code so well that you should use theirs. 
Bokeh is one of these libraries - it is library specifically with functions 
for making plots, charts, and graphs. 
It is based on the famous D3.js library originally developed at the New York Times for their visualizations, 
which has been used for many years to programmatically create visually appealing data visualizations.
When to make plots

We use plots to convey information. From this histogram:
You can immediately see that the US government spending has been steadily increasing, reaching a peak in January 2017.

So learning how to make plots will help you become better at displaying and communicating information, 
both to yourself and to others.
Plotting libraries in Python

If you are looking for a plotting library in Python, you have two main options: 
matplotlib and bokeh. Today I want to discuss bokeh, because I think it will become more popular in years to come.

Many Python developers (and especially data scientists and researchers) 
will tell you that the most commonly used plotting library in Python is matplotlib. 
I myself was a matplotlib user for many years - the integrations with Python data libraries are great, 
and migrating from the MATLAB plotting environment to matplotlib is easy. 
But a friend introduced me to bokeh and I was hooked ever since. 
Because it is based on D3.js, the visualizations look smooth and professional.

There is no one “best” plotting library - you should use whichever one feels and looks better for you. 
But for the rest of this post, I’ll talk about how to use bokeh to make a basic plot.

Installing bokeh

To use bokeh, we first have to install it. Unlike something like json or Counter from previous exercises, bokeh does not come installed with Python.

If you are using the Anaconda Python distribution (which you should, if you are on Windows!) then you can install bokeh by typing

conda install bokeh

in the Windows command prompt or the bash shell.

On OSX or GNU / Linux, just type

pip3 install bokeh

(If you have are using Python 2, you should do pip install bokeh.)


http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
'''
 
import pandas as pd
import json
import numpy as np
from pprint import pprint
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_file, show
from collections import Counter

#arr = np.array([])
name_list = []
birthday_list = []
add_recrod = {}
with open("birthdayJSON.json", "r") as f:
    birthdayDB = json.load(f)
    pprint(birthdayDB)
    #print(birthdayDB['Birthdays'][0]['name'])
    print(type(birthdayDB['Birthdays'][0]['name']))

    df = pd.DataFrame(birthdayDB)            #using panda DataFrame here. 
    print(df)
    #print(df["Birthdays"][0][['name','birthday']])
    #print(df["Birthdays"])
    print(df["Birthdays"][0]['name'])
    print(df["Birthdays"][0]['birthday'])
    
    #print(df["Birthdays"][1]['name'])
    loop = len(df["Birthdays"])
    print("List of people you can choose from: ")
    for i in range(0,loop):
        #print(df["Birthdays"][i]['name'])
        name_data = df["Birthdays"][i]['name']  ##this works
        birthday_data = df["Birthdays"][i]['birthday']
        #np.insert(arr,name_data)
        name_list.append(name_data)
        birthday_list.append(birthday_data)
        
        
    #print(name_list)
    #print(birthday_list)
    #print(type(name_list))
    name_array = np.asarray(name_list)
    birthday_array = np.asarray(birthday_list)
    #print(name_array)
    #print(type(name_array))
    index_df = pd.DataFrame({'index':[1,2,3,4,5]})
    
    name_df = pd.DataFrame({'names':name_array})
    birthday_df = pd.DataFrame({'birthday':birthday_array})
    #print(index_df)
    #print(name_df)
    #print(birthday_df)
    testing_df = pd.concat([name_df, birthday_df], sort=False, axis=1)
    #print(testing_df)
    #print(testing_df.index)
    print(f'This is the shape of the dataframe: {testing_df.shape}')
    print(testing_df.loc[0, "birthday"])
    #print(testing_df[0])
    #name_df = pd.append(index_df)
    #we are going to use pd.concat()function to join the dataframes
    #There are 3 Dataframes here: 1. index_df, 2. name_df 
    #index is for Identification, alignment and selection
    #pd.DataFrame(index = ['pbp'], columns = ['a','b'], dtype = np.dtype([('str','float')])) 
    df_empty = pd.DataFrame(['name', 'birthday'])
    
    
    #import numpy as np
    #myarray = np.asarray(mylist)
        
    #  numpy.insert(arr, obj, values, axis=None)[source]
########################################################################################
print("Welcome to the birthday dictionary. We know the birthdays of:")
print(name_df)
input_num = int(input("Please input an index next to the name to find out the birthday: "))
#print(type(input_num))
selected = testing_df.loc[input_num, 'names']
ans_record = testing_df.loc[input_num, 'birthday']
print(f'You have selected: {selected}')
print(f'The birtyday is: {ans_record}')

while True:
    additional_name = str(input("Please input a name of a famous person to add: "))
    print(f'You have inputted: {additional_name}')
    additional_birthday = input("Please input birthday of the person above:(example: Month, date, year => Jan 8, 2018)")
    print(f'You have inputted: {additional_birthday}')

    print(type(additional_birthday))
    #Store this as series or pd.series() instead...
    #add_series = pd.Series({'name':[additional_name], 'birthday':[additional_birthday]})
    add_series = pd.Series([additional_name, additional_birthday], index=['names','birthday'])

    #print(add_series)    #additional_record
    pprint(add_series)
    testing_df = testing_df.append(add_series, ignore_index = True)    ##here is the changed line
    #pprint(testing_df)
    
    more_data = input("Do you want to add more? (type: Y/N): ")
    more_data = more_data.lower()
    print(more_data)
    if more_data == 'y':
        continue
    else: 
        break
testing_df.to_json('modified_names.json')

############################# This is where 35 starts ###########################################

df_analysis = pd.read_json('modified_names.json')
#print(df_analysis)
#print(df_analysis.iloc[0]['birthday'])     #set the "birthday" column as a list then use Counter(list_name)

name_list = df_analysis['names'].tolist()  #use tolist() to convert a 'names' column and store it to name_list
#print(name_list)
birthday_list = df_analysis['birthday'].tolist()  #now converting birthday to a list
#print(birthday_list)
month_list = []
for element in birthday_list:
    split_by_mdy = element.split(' ')
    #print(split_by_mdy[0])
    month_list.append(split_by_mdy[0])
    
#print(month_list)
polished_mon = []
for element in month_list:
    if element =='January':
        element = 'Jan'
        polished_mon.append(element)
    elif element == "February":
        element = "Feb"
        polished_mon.append(element)
    elif element == "March":
        element = "Mar"
        polished_mon.append(element)
    elif element == "April":
        element = "Apr"
        polished_mon.append(element)
    elif element == "May":
        element = "May"
        polished_mon.append(element)
    elif element == "June":
        element = "June"
        polished_mon.append(element)
    elif element == "July":
        element = "Jul"
        polished_mon.append(element)
    elif element == "September":
        element = "Sept"
        polished_mon.append(element)
    elif element == "October":
        element = "Oct"
        polished_mon.append(element)
    elif element == "November":
        element = "Nov"
        polished_mon.append(element)
    elif element == "December":
        element = "Dec"
        polished_mon.append(element)
    else: 
        element = element
        polished_mon.append(element)
    
print("Here is a count of how many per each month for birthdays in the table")    
print(Counter(polished_mon))
stats_birthday = Counter(polished_mon)
print(type(stats_birthday))
new_stats_birthday = pd.DataFrame.from_dict(stats_birthday, orient='index').reset_index()
print(new_stats_birthday)
print(type(new_stats_birthday))
new_stats_birthday.to_json('birthday_stats.json')



############################Now Drawing using bokeh module ####################################
#fg = figure(x_axis_label ="", y_axis_label = "")    ## this comes as a default parameter (optional)w the figure()
base_data = pd.read_json('birthday_stats.json')
print(base_data)  #this works fine 
print(type(base_data))
'''
 index  0
0   Jan  2
1   Mar  1
2   Feb  1
3  June  2
4   Oct  1

column with month is the x axis
column with numbers is the y axis

'''

output_file("occurance_names_month.html", title="Bar graphs example")  #specifies the HTML output and where it goes

print(base_data.columns)
print(base_data['index'])
x_axis = base_data['index']
x = x_axis.tolist()    #looks like ['Jan', 'Mar', 'Feb', 'June', 'Oct']
print(f'Here is the x_axis and months: {x_axis}')


#now we need y axis data set
y_axis = base_data['0']      
y = y_axis.tolist()      #you need to specify x and y axis
print(f'Here is the y_axis and occurances: {y_axis}')
x_categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#create a figure
p = figure(x_range=x_categories)

#Create a histogram
p.vbar(x=x, top=y, width=0.5)

#displays 
show(p)

#Great link on how to do Histogram....go to bottom and follow the direction
#https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html
#Look at this link also. 
#https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4
#another great link!
#https://www.analyticsvidhya.com/blog/2015/08/interactive-data-visualization-library-python-bokeh/
