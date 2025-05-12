import streamlit as st
import requests

# Access the GitHub token from Streamlit secrets
GITHUB_TOKEN = st.secrets["github"]["token"]  # The token is stored as 'token' in secrets.toml

# Function to fetch files from GitHub
def fetch_files_from_github():
  url = "https://api.github.com/repos/Al-Jahed/Selective-Question-picker/contents/QuestionList"    headers = {
    "Authorization": f"token {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}"lace with your actual GitHub token
}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return list of files
    else:
      st.error(f"Error fetching files from GitHub: {response.status_code} - {response.text}")
        return []

# Streamlit interface
st.set_page_config(page_title="GitHub File Fetcher", layout="centered")
st.title("GitHub File Fetcher")

st.markdown("""
This app fetches files from a GitHub repository (`Selective-Question-picker`).
Click the button below to list the available files in the `QuestionList` folder.
""")

if st.button("Show Files from GitHub"):
    with st.spinner("Fetching files..."):
        files = fetch_files_from_github()

        if files:
            for file in files:
                st.write(f"- {file['name']}")  # Display the file names
        else:
            st.warning("No files found or there was an issue fetching the files.")
