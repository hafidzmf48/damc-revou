import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Path to the file in your Github repo
file_path = "https://raw.githubusercontent.com/hafidzmf48/damc-revou/main/Games%20Sales%20-%20Case%20Study%20-%20Games%20(1).csv"

# Read a CSV file using pandas
data = pd.read_csv(file_path, delimiter=',', encoding='utf-8', header=0)
data.drop_duplicates(inplace=True)
data['Series']=data['Series'].fillna('Non Series Game')
data['Release'] = pd.to_datetime(data['Release'])

st.set_option('deprecation.showPyplotGlobalUse', False)

# create sidebar
with st.sidebar:
  st.write("**My Profile**")
  img_path = "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/03731db4-f495-459f-b54f-09d4b1568d3a/original=true/00066-1676333655.jpeg"
  st.image(img_path)
  st.write('Hafidz Muhammad Fahri')
  st.write("""
           I am fresh graduate of statistics and have a passion of data visualization.
           Here i'm gonna test my skill by creating dashboard to analyze this dataset""")
  st.write('Variable contained in dataset :')
  column_names = data.columns.tolist()
  st.sidebar.markdown('### Columns:')
  for col in column_names:
    st.sidebar.write(col)

# create layout
    
st.title('**Games Sales Analysis** :video_game:')
st.header("Business Question", divider='blue')
st.write('1. Which games is the oldest and the newest in this dataset?')
st.write('2. Which publisher published most of the games?')
st.write('3. Which developer develop most of the games?')
st.write('4. Which series has the most sales?')
st.write('5. Which series has the most games?')

st.header("Visual Analyze", divider='blue')

# Answering Business Question
# answer question 1 with table
st.write('**The oldest game in dataset is** :')
oldest_game = data.sort_values(by='Release', ascending=True)
st.dataframe(oldest_game.head(1))
st.write('**The newest game in dataset is** :')
newest_game = data.sort_values(by='Release', ascending=False)
st.dataframe(newest_game.head(1))

st.write("Let's Answer Question 2,3,and 4 with histogram")

# create tabs that will contain various chart
tab1, tab2, tab3 = st.tabs(['Top Publisher','Top Developer','Top Games'])

with tab1 :
  st.header('Top 5 Publisher by Total Game Published')
  publishertop = data['Publisher'].value_counts().head(5)
  plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
  publishertop.plot(kind='bar')
  plt.xlabel('Publisher')
  plt.ylabel('Game Published')
  plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
  plt.tight_layout()
  st.pyplot()
  with st.expander("See explanation"):
    st.write("""
             The chart above show that **Electronic Arts** a.k.a **EA** has the most game publihed
             with total **19 games** had published.
    """)

with tab2 :
  st.header('Top 5 Developer by Total Game Developed')
  topdev = data['Developer'].value_counts().head(5)
  plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
  topdev.plot(kind='barh')
  plt.xlabel('Game Developed')
  plt.ylabel('Developer')
  plt.tight_layout()
  st.pyplot()
  with st.expander("See explanation"):
    st.write("""
             The chart above show that **Blizzard Entertainment** has the most game developed
             with total **8 games** had published.
    """)

with tab3 :
  st.header('Top 10 Sold Series')
  excluded_value = "Non Series Game"
  most_sold_series = data[data['Series'] != excluded_value].sort_values(by='Sales', ascending=False)
  topsales = most_sold_series.head(10)
  plt.figure(figsize=(10, 6))
  sns.barplot(topsales, x=topsales['Series'], y=topsales['Sales'], palette='coolwarm')
  plt.xlabel('Series')
  plt.ylabel('Sales')
  plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
  plt.tight_layout()
  st.pyplot()
  with st.expander("See explanation"):
    st.write("""
             The chart above show that **Minecraft** is the most sold games
             with total **33 games** sold.
    """)

st.write('Top 5 Series That Has Most Games :')
excluded_value = "Non Series Game"
series_counts = data[data['Series'] != excluded_value]['Series'].value_counts()
st.dataframe(series_counts.head(5))

text = st.text_area('Feedback')
st.write('Feedback: ', text)