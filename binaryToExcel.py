#!/usr/bin/env python
# coding: utf-8

# # Nick's Binary Data file for cycles
# 20220613 weg <br>

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'notebook')

import os, sys, logging, glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()


# In[2]:
num = str(9);
fname = 't' + num + '.bin'  # Looks like 4 byte data, ints, time(ms since epoch) and voltage(mV) .

# Data type with the binary format.  See page
# https://stackoverflow.com/questions/16573089/reading-binary-data-into-pandas

dt = np.dtype([('time', 'i4'), ('volts', 'i4')])  # datatype for reading binary
mydata = np.fromfile(fname, dt)  # numpy array
df = pd.DataFrame(mydata)  # pandas DataFrame


# In[3]:


df.head()


# In[4]:


print('size of array {}'.format(len(df.volts)))


# In[5]:


df['volts'].plot()


# In[6]:


fig, ax = plt.subplots()

ax.plot(df.volts[:73000])

plt.show()


# In[ ]:

#try:
    #with open('Sample', 'w') as f:
    #    f.write(df.head())
#except FileNotFoundError:
  #  print("The directory does not exist")

df.to_excel('sample' + num + '.xlsx')


# In[ ]:
