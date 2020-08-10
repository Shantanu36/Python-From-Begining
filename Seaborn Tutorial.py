#!/usr/bin/env python
# coding: utf-8

# ### Seaborn Tutorial

# #### Distrbution Plots  (for continuous features-numerical)
#   #Distplot
#   #Joinplot
#   #Pairplot

# #### Practise problems on IRIS Dataset

# In[5]:


import seaborn as sns


# In[6]:


df=sns.load_dataset("tips")


# In[7]:


df


# ### Corelation Using Heatmap

# #### only integer types are selected A corelation heatmap uses coloued cells,Typically in monochromatic scale,to show a 2D 
# #### matrixbetween two discrete dimensions or event types.It is very important in feature selection

# In[9]:


df.corr()  #only selects integer dimensions


# In[10]:


sns.heatmap(df.corr())


# ### JoinPlot

# #### it allows to study the relationship between 2 numeric variables.The central chart display their corelation.
# #### It is usually a scatter plot, a hexbin plot,2D Histogram or a 2D Density plot

# ### Biverate Analysis

# In[15]:


sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')


# In[16]:


sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')

# draws probability density function pdf curv around histogram curve and regression line inside box


# ### Pairplot(Scatterplot)

# #### One variable in the same data row is matched with another variables values,
# #### like this: pair plots are just elborations on this,showing all variables paired with all the other variables.

# In[17]:


sns.pairplot(df)


# In[19]:


sns.pairplot(df,hue='sex')


# ### Distplot

# #### It helps us to check the districution of the column feature

# In[29]:


sns.distplot(df['tip'])


# In[23]:


# the line is called KDE - Kernel density estimation


# In[28]:


sns.distplot(df['tip'],kde=False,bins=10)


# In[ ]:




