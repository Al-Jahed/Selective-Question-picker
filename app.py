import streamlit as st
import requests

# GitHub settings
GITHUB_REPO = "Al-Jahed/Selective-Question-picker"
FOLDER_PATH = "QuestionList"  # Path to the folder within the repo
GITHUB_TOKEN = "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"  # Paste your GitHub Token here

# Function to fetch the list of files from the specified folder in GitHub
def fetch_files_from_github():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{FOLDER_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json()
        file_names = [file['name'] for file in files if file['type'] == 'file']
        return file_names
    else:
        st.error(f"Error fetching files from GitHub: {response.status_code}")
        return []

# Streamlit app
st.title("📄 Question List from GitHub")

st.markdown("""
This app fetches and displays the files from the `QuestionList` folder in the GitHub repository.
Click the button below to load the list of available files.
""")

# Button to fetch the files from GitHub
if st.button("Show all files in the QuestionList folder"):
    with st.spinner("Fetching files..."):
        files = fetch_files_from_github()
        if files:
            st.write("### Available files:")
            for file in files:
                st.write(f"- {file}")
        else:
            st.warning("No files found or error fetching files.")
