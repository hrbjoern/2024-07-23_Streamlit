# https://github.com/hrbjoern/2024-07-23_Streamlit

import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title('hello st')

st.header('This is a header')

# st.subheader('This is a subheader')

# st.text('This is a text')


# im1 = '/home/hrbjoern/Desktop/Bildergedoens/Kritzlibaerchat.png'
# im2 = '/home/hrbjoern/Desktop/Bildergedoens/Mette_Fahrrad.jpg'

# #st.video('https://www.youtube.com/watch?v=9bZkp7q19f0')

# add_selectbox = st.sidebar.selectbox(
#     "Show images or vids?", 
#     ("Images", "Video"), 
# )

# # Display content based on selection
# if add_selectbox == "Images":
#     col1, col2 = st.columns(2)  # Create two columns
#     with col1:  # With the first column
#         st.image(im1, caption='Image 1')
#     with col2:  # With the second column
#         st.image(im2, caption='Image 2')
# elif add_selectbox == "Video":
#     col1, col2 = st.columns(2)  # Create two columns
#     with col1:  # With the first column
#         st.video('https://youtu.be/3IAo-5WxBzs?si=ifaj3ApTpgY04zIf')
#     with col2:  # With the second column
#         st.video('https://youtu.be/h7MoEcD_y98?si=3sEf8SDTygWBhIOt')


# Add a file uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    # To display the uploaded file, you need to check the file type.
    # For example, if it's an image:
    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    # st.image(df['total_cases'].plot())

    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot data from the DataFrame
    ax.plot(df.index, df['total_cases'])  # Assuming 'total_cases' is a column in your DataFrame

    # Set the title and labels
    ax.set_title('Total Cases Over Time')
    ax.set_xlabel('Index')
    ax.set_ylabel('Total Cases')

    # Display the plot
    st.pyplot(fig)

    # Khaled benutzte: 
    # st.scatter_chart(df, x=column1, y=column2)





