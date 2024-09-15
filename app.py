import os
import streamlit as st
import PyPDF2
import openai
from io import BytesIO

# Set your OpenAI API key (you can hardcode it here or set it using environment variables)
api_key = os.getenv("OPENAI_API_KEY")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page in range(len(pdf_reader.pages)):
        extracted_text += pdf_reader.pages[page].extract_text()
    return extracted_text

# Function to generate HTML resume using OpenAI's ChatCompletion API
def generate_html_resume(text_content, api_key):
    openai.api_key = api_key

    # OpenAI GPT ChatCompletion API call for HTML conversion
    prompt = f"Convert the following resume text into a professional HTML formatted resume:\n{text_content}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant that formats resumes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()

# Streamlit app starts here
st.title("LinkedIn PDF Resume to HTML Converter")

# File uploader for PDF file
uploaded_file = st.file_uploader("Upload your LinkedIn PDF resume", type="pdf")

# Optionally, allow the user to input their API key if it's not hardcoded or set in environment variables
if not api_key:
    api_key = st.text_input("Enter your OpenAI API key", type="password")

if uploaded_file is not None and api_key:
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(uploaded_file)

    # Generate HTML resume using OpenAI API
    with st.spinner("Generating HTML Resume..."):
        html_resume = generate_html_resume(pdf_text, api_key)
    
    # Display generated HTML for preview
    st.subheader("Generated HTML Resume")
    st.code(html_resume, language="html")

    # Allow user to download the HTML file
    st.download_button(
        label="Download HTML Resume",
        data=html_resume.encode('utf-8'),
        file_name="resume.html",
        mime="text/html"
    )
