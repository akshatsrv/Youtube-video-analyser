import streamlit as st
from youtubesearchpython import VideosSearch
import pandas as pd

# Set page title and favicon
st.set_page_config(
    page_title="YouTube Video Search",
    page_icon="🔍"
)

# Set page header
st.title("YouTube Video Search")

# Input for title
title_input = st.text_input("Enter the title to search for:")

# Function to search videos and save to CSV
def search_and_save_videos(title_input):
    videosSearch = VideosSearch(title_input, limit=5)
    results = videosSearch.result()["result"]
    df = pd.DataFrame(results)
    df.to_csv("videos.csv", index=False)

# Button to search and save
if st.button("Search and Save"):
    if title_input:
        search_and_save_videos(title_input)
        st.success("Videos searched and saved to 'videos.csv'")
    else:
        st.warning("Please enter a title to search for.")

# Download link for CSV file
if st.button("Download CSV"):
    with open("videos.csv", "rb") as file:
        st.download_button(
            label="Download CSV",
            data=file,
            file_name="videos.csv",
            mime="text/csv"
        )

# Display the contents of videos.csv as a table
try:
    df = pd.read_csv("videos.csv")
    st.write("### Videos found:")
    st.dataframe(df)
except FileNotFoundError:
    pass
