import streamlit as st
import requests

# Access the GitHub token from Streamlit secrets
# Ensure the secrets.toml file contains:
# [github]
# token = "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"
GITHUB_TOKEN = st.secrets["github"]["token"]

# Function to fetch files from GitHub
def fetch_files_from_github():
    url = "https://api.github.com/repos/Al-Jahed/Selective-Question-picker/contents/QuestionList"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"  # Using token securely from secrets
    }

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return list of files
        elif response.status_code == 401:
            st.error("Unauthorized access: Please check your GitHub token.")
        elif response.status_code == 403:
            st.error("API rate limit exceeded: Please wait or check your token permissions.")
        elif response.status_code == 404:
            st.error("Repository or path not found: Please verify the URL.")
        else:
            st.error(f"Unexpected error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while connecting to GitHub: {str(e)}")
    
    # Return an empty list if there was an issue
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
            st.write("### Files in `QuestionList` folder:")
            for file in files:
                # Display each file's name
                st.write(f"- {file.get('name')}")
        else:
            st.warning("No files found or an error occurred.")
