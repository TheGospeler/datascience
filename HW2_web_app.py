import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

# import the Iris dataframe
df_iris = sns.load_dataset("iris")

# What will be printed write-up
st.write("""
# Iris Dataset
What Specie has the longest petal_length?
""")

# Using the 3D scatter plot
fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=18,
              symbol='species', opacity=0.7)

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

# Plot using plotly
st.plotly_chart(fig, use_container_width=True)