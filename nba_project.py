#Import Libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from PIL import Image

import streamlit as st

# Add custom CSS to change the background color

st.markdown(
    """
    <style>
    body {
        background-color: #87CEEB;
        color: black;
    }

    .stApp {
        background-color: #87CEEB;
    }
    
    .stTextInput, .stTextArea, .stNumberInput, .stSelectbox, .stMultiselect, .stColorPicker {
        color: black;
        background-color: #B0E0E6;
    }
    
    .stButton, .stButton button {
        background-color: #B0E0E6;
        color: black;
    }
    
    .stButton:hover, .stButton button:hover {
        background-color: #ADD8E6;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Import mysql.connector - This provide all the database manipulation using python.
import mysql.connector as connection

#Set up the connection information
#Connect to "NBA" database.
#You should have installed the MYSQL Workbench on your local computer.
mydb = connection.connect(host="relational.fit.cvut.cz", database = "NBA",user = "guest", passwd="relational",use_pure=True)

# Display the Dataframe in a streamlit app
st.title("NBA Seasonal Championship")

# Display the banner picture in the streamlit app
img=Image.open("images1.jpg")
st.sidebar.image(img.resize((1200,780))) 


# Open the image
image = Image.open("NBA.jpg")

# Resize the image
resized_image = image.resize((500, 200))  # Change the dimensions (500, 0) as per your requirement

# Display the resized image
st.image(resized_image, use_column_width=True)

# Read SQL query or database table into python pandas Dataframe
ac=pd.read_sql_query('select * from Actions',mydb)
gm=pd.read_sql_query('select * from Game',mydb)
tm=pd.read_sql_query('select * from Team',mydb)
pl=pd.read_sql_query('select * from Player',mydb)

# Merge the DataFrames based on a common column
data1 = pd.merge(ac, gm)
data2 = pd.merge(data1, tm)
data3 = pd.merge(data2, pl)


# Display the merged DataFrame in Streamlit
st.write(data3)

# Add a sidebar with filter options


st.sidebar.title("GAMES")
GAMES = st.sidebar.selectbox('Select Game', data1["GameId"].unique())
filter_data1= data1[(data1["GameId"]==GAMES)]
st.write(filter_data1)

st.sidebar.title("TEAMS")
TEAMS = st.sidebar.selectbox('Select Team', data2["TeamName"].unique())
filter_data2= data2[(data2["TeamName"]==TEAMS)]
st.write(filter_data2)

st.sidebar.title("PLAYERS")
PLAYERS = st.sidebar.selectbox('Select Player', data3["PlayerName"].unique())
filter_data3= data3[(data3["PlayerName"]==PLAYERS)]
st.write(filter_data3)


# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(filter_data1['Points'], filter_data1['TeamId'])  # Replace 'SomeColumn' with the column you want to plot

# Set labels and title
plt.xlabel('Points')
plt.ylabel('TeamId')
plt.title('Bar Chart')

# Display the chart
st.pyplot(plt)
