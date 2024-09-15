# LinkedIn_Pdf_to_HTML_page

Link to the APP: https://linkedinpdftohtmlpage-3r8ywvvedmtbuac9jbszri.streamlit.app/



# 1. Understanding the Problem
The problem involves creating a web application that:

Allows users to upload a PDF file.
Extracts text from the uploaded PDF.
Converts the extracted text into an HTML resume using OpenAI’s GPT model.
Provides the HTML resume for preview and download.
# 2. Designing the Solution
Components of the Solution:

PDF Text Extraction: Extract text from the uploaded PDF file.
HTML Resume Generation: Use OpenAI’s API to convert the extracted text into an HTML-formatted resume.
Streamlit Interface: Provide a user interface for file upload, API key input, and display/download of the HTML resume.
# Steps to Achieve This:

1.Setting Up the Environment

Import necessary libraries: os for environment variables, streamlit for the web app interface, PyPDF2 for PDF text extraction, openai for API interaction, and io for handling file-like objects.

2.Extract Text from PDF

Define a function extract_text_from_pdf to read the PDF file using PyPDF2 and concatenate text from each page.

3.Generate HTML Resume

Define a function generate_html_resume to send a prompt to OpenAI’s API, requesting the conversion of text to HTML.
Use the ChatCompletion.create method to interact with the GPT model, passing the prompt and receiving HTML-formatted text.

4.Streamlit Interface

Set up the Streamlit app with a title and a file uploader to handle PDF file uploads.
Optionally, prompt users to input their OpenAI API key if not already set.
On file upload and API key input, extract text from the PDF and call the HTML generation function.
Display the generated HTML in a code block and provide a download button for the HTML file.

# Explanation of the Code
Imports: Essential libraries are imported for file handling, web interface creation, text extraction, and API interaction.
API Key Handling: The API key is retrieved from environment variables or user input.
Text Extraction: The function extract_text_from_pdf reads each page of the PDF and extracts text.
HTML Generation: The function generate_html_resume formats the extracted text into HTML using OpenAI’s API.
Streamlit Interface: Provides a user-friendly interface for file upload, API key input, and preview/download of the HTML resume.

This approach ensures that users can easily convert their LinkedIn PDFs into HTML resumes with minimal effort, leveraging powerful tools like OpenAI’s GPT for professional formatting.
