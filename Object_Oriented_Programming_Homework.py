#!/usr/bin/env python
# coding: utf-8

# ### Homework Assignment 

# #### Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tupples and return the slope and distance of the line

# In[61]:


import math

class Line():
    
    def __init__(self,coor1,coor2):
        
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2-x1)**2+(y2-y1)**2)             
        #formula for distance << d= SQRt(x2-x1)^2+(y2-y1)^2
    
    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((y2-y1)/(x2-x1))


# In[62]:


li = Line((1,2),(3,4))


# In[63]:


li.coor1


# In[64]:


li.coor2


# In[65]:


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[66]:


li.distance()


# In[67]:


li.slope()


# #### Problem 2

# Fill in the class

# In[85]:


import math


class Cylinder():
    pi=3.14
    def __init__(self,height = 1, radius = 1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        height = self.height
        radius = self.radius
        return self.pi * radius **2 *height
                 #formula for the volume of cylinder is piR^2H 
    
    def surface_area(self):
        height = self.height
        radius = self.radius
        top = self.pi * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)
            #formula for the surface area of a cylinder is 2piRH
        


# In[86]:


c = Cylinder(2,3)


# In[87]:


c.volume()


# In[88]:


c.surface_area()


# In[ ]:




