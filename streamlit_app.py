
import streamlit as st
import json
import uuid
import os
from PyPDF2 import PdfReader



def read_pdf(file):
    pdfReader = PdfReader(file)
    information = pdfReader.metadata
    number_of_pages = pdfReader.pages
    all_page_text = ""

    pdf_infos = {"Author": {information.author},
        "Creator": {information.creator},
        "Producer": {information.producer},
        "Subject": {information.subject},
        "Title": {information.title},
        "Number of pages": {len(number_of_pages)}}

    return pdf_infos

# genre list
genre_list = ["", "immersion", "culture", "health", "activities", "dietary lifestyles", "cookbooks", "other"]



st.subheader("Upload a vegan book 🌱 📗")

with st.form("Upload a vegan book🌱📗" ):


    col1, col2 = st.columns(2)

    with col1:

        title = st.text_input("Title" , key="2")
        author = st.text_input("Author" , key="3")

    with col2:

        placeholder_genre = st.empty()
        placeholder_other_genre = st.empty()


    st.markdown("##")
    st.subheader("Upload PDF")


    uploaded_file = st.file_uploader('upload pdf', type=["pdf"])
    submit = st.form_submit_button(f"submit file info")

    if uploaded_file:

        st.write(f"detected information: {read_pdf(uploaded_file)}")


        if submit:

            if title and author and genre:

                sample_uid = str(uuid.uuid4())[:8]

                file_name = f"{sample_uid}_{title.lower().replace(' ', '_')}.pdf"

                dic_set = {
                    sample_uid: {"title": title, "genre": genre, "sample_uid": sample_uid,
                                 "author": author}
                           }
                # save to some db
                st.success(f" {'pdf sent!'} `{file_name}`")
                st.text(f"submitted: {sample_uid}, {title}, {author}, {genre}")


            else:
                st.warning("Missing fields")



with placeholder_genre:

    genre = st.selectbox("Genre", options=genre_list, key="4")

with placeholder_other_genre:
    if genre == "other":
        genre = st.text_input(f"enter other genre")






    # # Then get the data at that reference.
    # doc = doc_ref.get()
    #
    # # Let's see what we got!
    # st.write("The id is: ", doc.id)
    # st.write("The contents are: ", doc.to_dict())
