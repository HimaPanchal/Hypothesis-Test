#!/usr/bin/env python
# coding: utf-8

# # Independent Sample T- Test and Welch's Test (use this by default)

# In[18]:


# Import required packages 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import ttest_ind, norm


# In[19]:


sample_A = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)
sample_B = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)


# In[20]:


plt.hist(sample_A, density= True, alpha = 0.05)
plt.hist(sample_B, density= True, alpha = 0.05)
plt.show()


# In[21]:


sample_A_mean = sample_A.mean()
sample_B_mean = sample_B.mean()
print(sample_A_mean, sample_B_mean)


# In[22]:


null_hypothesis = "The mean of the sample A is equals to that of the mean of the sample B"
alternate_hypothesis = "The mean of the sample A is different than that of the mean of the sample B"
acceptance_criteria = 0.05


# In[23]:


t_statistics, p_value = ttest_ind(sample_A, sample_B)
print(t_statistics, p_value)


# In[24]:


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis")
else: 
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we fail to reject the null hypothesis and conclude that the mean of the sample is equal to the mean of Population")


# In[25]:


# Welch's Test is more reliable and it should be selected by default in comparison  ttohe Independent Sample T-Test
t_statistics, p_value = ttest_ind(sample_A, sample_B, equal_var = False)
print(t_statistics, p_value)


# In[26]:


# p-value test for the Welch's Test 
if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis")
else: 
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we fail to reject the null hypothesis and conclude that the mean of the sample is equal to the mean of Population")

