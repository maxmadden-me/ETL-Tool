#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

st.write("""
#My First App
Hello *World!*
""")

d = {"Value":[1,2,3],
    "Number":[4,5,6]}
df = pd.DataFrame(d)

st.line_chart(df)


# In[ ]:





# In[ ]:




