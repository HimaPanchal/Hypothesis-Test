#!/usr/bin/env python
# coding: utf-8

# # One Sample T- Test (Hypothesis Test) with Mock Data

# In[19]:


# Import required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, norm


# In[20]:


# Create Mock data 
population = norm.rvs(loc=500, scale= 100, size = 1000, random_state = 42).astype(int)
np.random.seed(42)


# In[21]:


sample = np.random.choice(population,250)
plt.hist(population, density= True, alpha = 0.5)
plt.show()


# In[22]:


population_mean = population.mean()
sample_mean = sample.mean()
print(population_mean, sample_mean)


# In[23]:


# Set the Hypothesis Test and Acceptance Criteria
null_hypothesis = "The mean of the sample is equal to the mean of the Population"
alternate_hypothesis = "The mean of the sample is different than the mean of the Population"
acceptance_criteria = 0.05


# In[24]:


# Execute the Hypothesis test
t_statistic, p_value = ttest_1samp(sample, population_mean)
print(t_statistic, p_value)


# In[25]:


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis")
else: 
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we fail to reject the null hypothesis and conclude that the mean of the sample is equal to the mean of Population")


# In[ ]:





# In[ ]:




