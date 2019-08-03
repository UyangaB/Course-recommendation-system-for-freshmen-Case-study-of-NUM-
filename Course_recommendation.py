#!/usr/bin/env python
# coding: utf-8

# Read the first csv file


import pandas as pd
import scipy as sc
from pandas import DataFrame
from scipy import integrate
user_data = pd.read_csv(r"C:\Users\user\Documents\TestDataset\Datasets\\userbased.csv")
user_data.head()


# Find the sample user


sample_user = user_data.sample(1)
df_of_sample_user = DataFrame(sample_user, columns = ['SID', 'scaledScore', 'FK_School', 'Gender'])
df_of_sample_user


# Find the other user


df_of_other_user = DataFrame(user_data, columns = ['SID', 'scaledScore', 'FK_School', 'Gender'])
df_of_other_user


# Calculate the distance between the sample user and other user


df_of_distance = pd.DataFrame({'SID': [], 'Dist': []})
for i in range(len(df_of_other_user)):
    df_of_distance = df_of_distance.append (
        {'SID':  df_of_other_user.iloc[i]['SID'], 
         'Dist': sc.spatial.distance.cdist(df_of_sample_user.iloc[0:,1:], df_of_other_user.iloc[i:i+1,1:], metric='euclidean')}
        ,ignore_index=True )
    


# Find the smallest distance


lowest_distance_11 = df_of_distance.sort_values(by=['Dist']).head(11)
lowest_distance_11

lowest_distance_10 = lowest_distance_11.drop([4276], axis=0).head(10)
lowest_distance_10


# Read the second CSV file


course_data = pd.read_csv(r"C:\Users\user\Documents\TestDataset\Datasets\\coursebased.csv")
course_data.head()


# To the dataframe


df_of_course_data = DataFrame(course_data, columns = ['SID', 'teacherid', 'courseid', 'Credit', 'offeredyear', 'offeredsemester', 'totalscore', 'result_word'])


# Combine the values i've got


merge_data = pd.merge(df_of_course_data,lowest_distance_10, on='SID')
merge_data

sorted_merge_data = merge_data.sort_values(by=['Dist'])
sorted_merge_data


# In[49]:


course_with_high_score = sorted_merge_data[sorted_merge_data['totalscore'].notnull() & (sorted_merge_data['totalscore'] > 90)]


# In[50]:


course_with_high_score


# In[51]:


course_with_high_score.drop_duplicates(['courseid'])


# In[52]:


course_high_score_five = course_with_high_score.sort_values(by=['totalscore']).head(5)


# In[53]:


course_high_score_five


# In[54]:


course_info = pd.read_csv(r"C:\Users\user\Documents\TestDataset\Datasets\\course_information.csv")


# In[55]:


course_info_of_five = pd.merge(course_high_score_five, course_info, on='courseid')


# In[56]:


result = course_info_of_five[['courseid','SubjectID','Subject','Credit_y']]


# In[57]:


result


# In[58]:


course_of_sample_user = pd.merge(df_of_sample_user,df_of_course_data, on='SID')
course_of_sample_user
course_of_sample_user_col = course_of_sample_user[['courseid']]
course_of_sample_user_col
course_info_of_five_col = course_info_of_five[['courseid']]
course_info_of_five_col
approximate = course_of_sample_user_col.corrwith(course_info_of_five_col)
approximate


# In[59]:


course_of_sample_user


# In[60]:


course_of_sample_user_col = course_of_sample_user[['courseid']]
course_of_sample_user_col


# In[61]:


course_info_of_five_col = course_info_of_five[['courseid']]
course_info_of_five_col


# In[62]:


approximate = course_of_sample_user_col.corrwith(course_info_of_five_col)


# In[63]:


approximate


# In[64]:


df_of_other_courses = DataFrame(course_data, columns = ['SID', 'teacherid', 'courseid', 'Credit', 'offeredyear', 'offeredsemester', 'totalscore', 'result_word'])


# In[65]:


df_of_sample_courses = DataFrame(course_of_sample_user, columns = ['SID', 'teacherid', 'courseid', 'credit', 'offeredyear', 'offeredsemester', 'totalscore', 'result_word'])


# In[66]:


distance_of_courses = pd.DataFrame({'courseid': [], 'dist': []})
for i in range(len(df_of_other_courses)):
    distance_of_courses = df_of_distance.append (
        {'courseid':  df_of_other_courses.iloc[i]['courseid'], 
         'dist': sc.spatial.distance.cdist(df_of_sample_courses.iloc[0:,1:], df_of_other_courses.iloc[i:i+1,1:], 
                                           metric='euclidean')}
        ,ignore_index=True )
    


# In[67]:


distance_of_courses


# In[ ]:




