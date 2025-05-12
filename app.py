import streamlit as st
import requests
from docx import Document
from io import BytesIO

# Streamlit page setup
st.set_page_config(page_title="📘 GitHub DOCX Viewer", layout="centered")
st.title("📘 Select and View DOCX Files from GitHub")

st.markdown("""
This app lists `.docx` files from your GitHub repo's `QuestionList/` folder and displays their contents.
""")

# GitHub Repo Information
GITHUB_USER = "Al-Jahed"
REPO_NAME = "Selective-Question-picker"
FOLDER_PATH = "QuestionList"
BRANCH = "main"  # Change to "master" if your branch name is different

# GitHub API to list folder contents
api_url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FOLDER_PATH}?ref={BRANCH}"

# Request list of files from GitHub
response = requests.get(api_url)

if response.status_code == 200:
    files = response.json()
    docx_files = [f for f in files if f["name"].endswith(".docx")]

    if docx_files:
        file_names = [f["name"] for f in docx_files]
        selected_name = st.selectbox("📂 Select a DOCX file", file_names)

        selected_file = next(f for f in docx_files if f["name"] == selected_name)
        download_url = selected_file["download_url"]

        file_response = requests.get(download_url)
        if file_response.status_code == 200:
            doc = Document(BytesIO(file_response.content))
            content = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
            st.text_area(f"📄 Contents of `{selected_name}`", content, height=400)
        else:
            st.error("❌ Failed to download the selected file.")
    else:
        st.warning("⚠️ No `.docx` files found in the folder.")
else:
    st.error("❌ Unable to access GitHub folder. Make sure the repo and folder are public.")
