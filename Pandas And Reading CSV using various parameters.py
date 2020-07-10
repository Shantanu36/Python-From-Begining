#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


from pandas import ExcelWriter
from pandas import ExcelFile


# In[54]:


df=pd.read_csv ('C:/Users/Shanty/Desktop/Python Start to End/sample.csv')


# In[55]:


df.head()


# In[56]:


df=pd.read_csv ('C:/Users/Shanty/Desktop/Python Start to End/test1.csv')


# In[57]:


df.head()  # Selects 5 rows


# In[58]:


df.info()


# In[59]:


df.describe()  #only takes numerical(object) columns into consideration and not categorical or alphabetic features 


# In[64]:


df['X0'].value_counts()


# ## CSV

# In[69]:


from io import StringIO,BytesIO


# In[74]:


Data=('column1,column2,column3,column4,column5\n'
'r0,1,2,3,4,5\n'
'r1,6,7,8,9,10\n'
'r2,2,3,4,5,6\n'
'r3,4,5,6,7,8\n')


# In[75]:


type('Data')


# In[76]:


pd.read_csv(StringIO(Data))


# In[78]:


df=pd.read_csv(StringIO(Data),usecols=['column1','column4'])


# In[79]:


df.to_csv('jupyterCSV')


# In[86]:


Data=('a,b,c,d\n'
     '1,2,3,4\n'
     '5,6,7,8\n'
      '9,10,11,12\n')

print(Data)
# In[87]:


df1=pd.read_csv(StringIO(Data),dtype=int)


# In[88]:


df1


# In[89]:


df1['a']


# In[91]:


df1['a'][1]


# In[94]:


df1=pd.read_csv(StringIO(Data),dtype={'a':int,'b':'float','c':str})


# In[101]:


df1


# In[103]:


type(df1['b'][2])


# In[106]:


df1['b']


# ### Providing Index Column to Data

# In[4]:


import pandas as pd
import numpy as np
from io import StringIO,BytesIO


# In[50]:


Data1=('a,b,c\n'
      '4,apple,cat\n'
      '5,mango,dog\n'
      '6,chiku,rat')


# In[51]:


print(Data1)


# In[52]:


df2=pd.read_csv(StringIO(Data1),dtype={'a':int,'b':str,'c':str})


# In[54]:


df2


# In[55]:


df3=pd.read_csv(StringIO(Data1))


# In[56]:


print(df3)


# In[8]:


Data2=('a,b,c\n'
      '4,apple,cat\n'
      '5,mango,dog\n'
      '6,chiku,rat\n'
      '7,peru,parrot')


# In[9]:


print(Data2)


# In[10]:


df4=pd.read_csv(StringIO(Data2))
print(df4)


# In[11]:


df4=pd.read_csv(StringIO(Data2),usecols=['b','c']) #displayes only column b & c along with index column
print(df4)


# In[13]:


df4=pd.read_csv(StringIO(Data2),usecols=['b','c'],index_col='c') # uses column 'C' As an index(1st) column)
print(df4)


# ### Quoting and Escape Charecters,Usefull for NLP

# In[15]:


Data='a,b\n"hello,\\"bob\\",nice to see you",6'


# In[16]:


df5=pd.read_csv(StringIO(Data),escapechar='\\')


# In[17]:


df5


# ### URL To CSV

# In[19]:


df6=pd.read_csv('https://www.myonlinetraininghub.com/excel-tabular-data-format',SEP='/t')


# In[ ]:





# In[1]:


csvRead=pd.read_csv('C:/Users/Shanty/Desktop/Python Start to End/283186_583426_bundle_archive/test.csv')


# In[50]:


csvRead


# In[ ]:




