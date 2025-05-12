import streamlit as st
import requests
from docx import Document
from io import BytesIO

# --- Page Setup ---
st.set_page_config(page_title="📘 Question File Selector", layout="centered")
st.title("📘 Selective Question Picker")

# --- GitHub Repo Info ---
GITHUB_USER = "Al-Jahed"
REPO_NAME = "Selective-Question-picker"
FOLDER_PATH = "QuestionList"
BRANCH = "main"

api_url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FOLDER_PATH}?ref={BRANCH}"

response = requests.get(api_url)

if response.status_code == 200:
    files = response.json()
    # Process files
else:
    st.error(f"Error {response.status_code}: Unable to access the folder. Please check the repository and folder settings.")

# --- Show Button to Display Files ---
if st.button("📂 Show Available Files"):
    with st.spinner("Fetching file list..."):
        response = requests.get(api_url)

    if response.status_code == 200:
        files = response.json()
        docx_files = [f for f in files if f["name"].lower().endswith(".docx")]

        if not docx_files:
            st.warning("⚠️ No `.docx` files found in the `QuestionList` folder.")
        else:
            file_names = [f["name"] for f in docx_files]
            selected_name = st.selectbox("Select a file to view:", file_names)

            # Get the download URL of selected file
            selected_file = next(f for f in docx_files if f["name"] == selected_name)
            download_url = selected_file["download_url"]

            # Download and read the docx content
            file_response = requests.get(download_url)
            if file_response.status_code == 200:
                doc = Document(BytesIO(file_response.content))
                content = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
                st.text_area(f"📄 Contents of `{selected_name}`", content, height=400)
            else:
                st.error("❌ Failed to download the selected file.")
    else:
        st.error("❌ Unable to access GitHub folder. Make sure the repo and folder are public.")
else:
    st.info("Click the button above to load `.docx` files from your GitHub folder.")
