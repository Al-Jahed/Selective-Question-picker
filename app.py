import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load the .env file to get the GitHub token
load_dotenv()

# GitHub token from the environment variable
GITHUB_TOKEN = os.getenv("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")

# GitHub repository details
GITHUB_OWNER = "Al-Jahed"
GITHUB_REPO = "Selective-Question-picker"
FOLDER_PATH = "QuestionList"  # The folder in the repo

# Function to fetch files from the QuestionList folder in the GitHub repo
def fetch_files_from_github():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{FOLDER_PATH}"
    
    headers = {
        "Authorization": f"token {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}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        files = response.json()
        file_names = [file['name'] for file in files if file['type'] == 'file']  # Get file names only
        return file_names
    else:
        st.error(f"Error fetching files: {response.status_code}")
        return []

# Streamlit UI
st.title("📁 Display Files in 'QuestionList' Folder")

# Button to trigger file listing
if st.button('Show Files in QuestionList'):
    st.write("Fetching files from GitHub...")
    files = fetch_files_from_github()
    
    if files:
        st.write("### Available Files:")
        for file in files:
            st.write(f"- {file}")
    else:
        st.write("No files found or there was an error.")
