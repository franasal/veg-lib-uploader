import streamlit as st
from PyPDF2 import PdfReader
import uuid

# Function to read PDF metadata
def read_pdf_metadata(file):
    pdf_reader = PdfReader(file)
    information = pdf_reader.metadata
    number_of_pages = len(pdf_reader.pages)

    pdf_infos = {
        "Author": information.author,
        "Creator": information.creator,
        "Producer": information.producer,
        "Subject": information.subject,
        "Title": information.title,
        "Number of pages": number_of_pages
    }

    return pdf_infos

# List of genre options
genre_list = ["", "immersion", "culture", "health", "activities", "dietary lifestyles", "cookbooks", "other"]

# Streamlit UI
st.subheader("Upload a vegan book 🌱 📗")

with st.form("Upload a vegan book🌱📗"):
    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input("Title", key="2")
        author = st.text_input("Author", key="3")

    with col2:
        placeholder_genre = st.empty()
        placeholder_other_genre = st.empty()

    st.markdown("##")

    uploaded_file = st.file_uploader('Upload PDF', type=["pdf"])
    submit = st.form_submit_button(f"Submit file info")

    if uploaded_file:
        pdf_metadata = read_pdf_metadata(uploaded_file)
        st.write(f"Detected information: {pdf_metadata}")

with placeholder_genre:
    genre = st.selectbox("Genre", options=genre_list, key="4")

with placeholder_other_genre:
    if genre == "other":
        genre = st.text_input("Enter other genre")


if submit:
    if title and author and genre:
        sample_uid = str(uuid.uuid4())[:8]
        file_name = f"{sample_uid}_{title.lower().replace(' ', '_')}.pdf"

        book_info = {
            sample_uid: {
                "title": title,
                "genre": genre,
                "sample_uid": sample_uid,
                "author": author
            }
        }
        # Save book_info to a database or appropriate storage
        st.success(f"PDF sent! `{file_name}`")
        st.text(f"Submitted: {sample_uid}, {title}, {author}, {genre}")
    else:
        st.warning("Missing fields")
