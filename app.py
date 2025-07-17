import streamlit as st
from summarizer import summarize_text
from file_handler import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

st.title("📄 AI Document Summarizer (Attenborough Style)")

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    # Extract text based on file type
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(uploaded_file)
    else:
        text = extract_text_from_txt(uploaded_file)

    st.text_area("Extracted Text", text[:3000], height=300)

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("🎙️ Summary (David Attenborough Style)")
        st.write(summary)
