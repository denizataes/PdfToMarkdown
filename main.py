import streamlit as st
import sys
import os
from parser import Parser
import sys
import post_proc
from os.path import isfile, join, exists, abspath
from os import listdir, makedirs
import txt_ext
from sspipe import p
import pre_proc 
import outlines
import ntpath
from pdfminer.pdfparser import PDFSyntaxError
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed


def control_PDF(pdf_docs):
    if(len(pdf_docs) <= 0):
        st.warning('Please select at least 1 pdf document!', icon="⚠️")
        return

def convert_PDF(pdf_docs):
    for pdf in pdf_docs:
        if pdf is not None:
            pdf_name = pdf.name  
            
            pdf_name_without_extension = os.path.splitext(pdf_name)[0]

            folder_path = os.path.join("Markdowns", pdf_name_without_extension)
            os.makedirs(folder_path, exist_ok=True)

            extract_and_process(
                folder_path,
                pdf_name,
                pdf.read())
            
            st.success(pdf_name_without_extension + ".md successfully converted.", icon="✅")


def process_html(raw_html_text):
	"""Processes hmtl raw text (originally a pdf) and gets rid of
		unnecessary elements, keeping the text content in it.

	Args:
		raw_html_text (string): html text to be processed.

	Returns:
		string: html text once is processed.
	"""
	bounds_list = pre_proc.get_page_bounds(raw_html_text)

	processed_text_html = ( pre_proc.split_spans(raw_html_text) 	| p(pre_proc.delete_non_textual_elements)
																	| p(pre_proc.delete_headers, bounds_list)
																	| p(pre_proc.delete_vertical_text)
																	| p(pre_proc.sort_html)
		)
	return processed_text_html

def process_md(text_md):
	"""Processes document as MarkDown text, so it reconstructs the 
		title-content structure of the document.

	Args:
		processed_text_html (string): markdown text to be processed.

	Returns:
		string: markdown text once is processed.
	"""
	processed_text_md = ( pre_proc.replace_br(text_md)
														| p(pre_proc.remove_false_titles)
														| p(pre_proc.remove_blank_lines)
														| p(pre_proc.replace_cid)
														| p(pre_proc.replace_with_dash)
														| p(pre_proc.join_by_hyphen)
														| p(pre_proc.join_lines)
														| p(pre_proc.join_lines)
														| p(pre_proc.join_et_al)
														| p(pre_proc.join_beta)
														| p(pre_proc.join_vs)
														| p(pre_proc.fix_enye)
														| p(pre_proc.join_ellipsis)
														| p(pre_proc.join_subtraction)
														| p(pre_proc.join_by_colon)
														| p(pre_proc.remove_duplicated_dashes)
														| p(pre_proc.fix_marks)
														| p(pre_proc.join_title_questions)
														| p(pre_proc.remove_useless_lines)
														| p(pre_proc.remove_duplicated_whitespaces)
														| p(pre_proc.remove_repeated_strings)
														
		)
	return processed_text_md

def process(text, output_dir, file_name):
	# Process HTML
	processed_text_html = process_html(text)
	
	# Convert HMTL to MD
	text_md = pre_proc.extract_text_md(processed_text_html)

	# Process MD
	processed_text_md = process_md(text_md)
	
	pre_proc.create_text_file(output_dir + "/" + file_name + ".md", processed_text_md) 


def extract_and_process(input_dir, pdf_name, pdf_content):
    st.info('Extracting text from: ' + pdf_name)
    try:
        # Extract PDF to HTML format
        extracted_text = txt_ext.extract_pdf_to_html(pdf_content)
        # Write raw HTML
        st.info("Extraction finished: " + pdf_name + " \n\n Starting processing...")
        process(extracted_text, input_dir, pdf_name)
        st.info("Processing finished!")
    except PDFSyntaxError:
        st.warning("PDFSyntaxError: Is this really a PDF? " + pdf_name)
    except PDFTextExtractionNotAllowed as e:
        st.warning(e)

def main():
    #load_dotenv() 
    
    st.set_page_config(page_title="Convert PDF to Markdown", page_icon=":books:")
    #st.write(css, unsafe_allow_html=True)
    st.subheader("Your Documents")
    pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files= True)
    
    if st.button("Convert"):
        with st.spinner("Converting PDF to Markdown..."):
            
            control_PDF(pdf_docs)
            convert_PDF(pdf_docs)

if __name__ == '__main__':
    main()




