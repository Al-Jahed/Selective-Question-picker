import streamlit as st
import os
import requests

# Set page configuration
st.set_page_config(page_title="Question List Viewer", layout="centered")
st.title("📘 Display Available Questions")

# URL to your GitHub repository's folder
GITHUB_REPO_URL = 'https://raw.githubusercontent.com/yourusername/yourrepository/main/QuestionList/'

# Function to fetch files from the folder
def fetch_files_from_github():
    # Get the file list from GitHub (raw URL)
    file_url = GITHUB_REPO_URL + 'Prep.docx'  # Adjust if you have multiple files
    response = requests.get(file_url)
    
    # Check if file exists and return its content
    if response.status_code == 200:
        return response.text  # Returns the raw text of the file
    else:
        return "Error: Unable to fetch file from GitHub"

# Buttons for actions
st.markdown("""
Please choose an action below:
""")

# Button A: Search box (you can implement this later)
if st.button("Button A: Search Box"):
    st.write("You chose to search the file. This feature will be implemented later.")

# Button B: Show all files in the folder (this will display the questions in the file)
if st.button("Button B: Show All Files in Folder"):
    with st.spinner("Fetching questions..."):
        questions = fetch_files_from_github()
        
    if questions:
        st.success("Questions fetched successfully!")
        st.text_area("Questions from Prep.docx", questions, height=300)
    else:
        st.error("Could not retrieve the questions.")
