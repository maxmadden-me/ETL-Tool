#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:      
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
     
st.write("""
#My First App
Hello *World!*
""")



#d = {"Value":[1,2,3],
    #"Number":[4,5,6]}
df = pd.DataFrame(dataframe)

st.line_chart(df)


# In[ ]:





# In[ ]:




