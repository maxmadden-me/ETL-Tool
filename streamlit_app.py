#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)
else:
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




