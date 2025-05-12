import streamlit as st
import requests

# Set up the page configuration
st.set_page_config(page_title="Question File Selector", layout="centered")
st.title("📑 Select and Display Question Files")

# GitHub repository URL and folder path
GITHUB_REPO = "https://api.github.com/repos/Al-Jahed/Selective-Question-picker/contents/QuestionList"

# Function to get files from the GitHub folder
def fetch_files_from_github():
    try:
        # Fetching the contents of the folder (QuestionList) from GitHub
        response = requests.get(GITHUB_REPO)
        response.raise_for_status()
        files = response.json()

        # Filtering out the directories and listing the file names
        file_list = [file['name'] for file in files if file['type'] == 'file']
        return file_list
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching files from GitHub: {e}")
        return []

# Streamlit user interface for selecting and displaying files
st.markdown("""
    This app will show all the available question files in the `QuestionList` folder.
""")

# Button to fetch and display all files
if st.button("Show All Files in QuestionList"):
    with st.spinner("Fetching files from GitHub..."):
        file_list = fetch_files_from_github()
        
        if file_list:
            st.write("### Files Available in QuestionList:")
            for file_name in file_list:
                st.write(f"- {file_name}")
        else:
            st.warning("No files found in the `QuestionList` folder or unable to fetch files.")
else:
    st.info("Click the button to see the files in the `QuestionList` folder.")
