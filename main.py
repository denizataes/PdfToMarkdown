import streamlit as st
#from PyPDF2 import PdfReader # for pdf read
import os
import aspose.words as aw
#import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
#from docx import Document as aw
import sys
import os
from parser import Parser
from writer import Writer
from syntax import UrbanSyntax



def control_PDF(pdf_docs):
    if(len(pdf_docs) <= 0):
        st.warning('Please select at least 1 pdf document!', icon="⚠️")
        return

def convert_PDF(pdf_docs):
    for pdf in pdf_docs:
        if pdf is not None:
            pdf_name = pdf.name  # PDF dosyasının adını alın
            
            # PDF'nin adında bulunan uzantıyı kaldırarak temiz bir dosya adı elde edin
            pdf_name_without_extension = os.path.splitext(pdf_name)[0]
            print(pdf_name_without_extension + " convertiong to md.")

            # Yeni bir klasör oluşturun (Markdowns/pdfs_adı)
            folder_path = os.path.join("Markdowns", pdf_name_without_extension)
            os.makedirs(folder_path, exist_ok=True)

            # PDF dosyasını işlemek için doküman nesnesini oluşturun
            #doc = aw.Document(pdf)

            # Klasör içinde Output.md olarak kaydedin
            #output_path = os.path.join(folder_path, pdf_name_without_extension + ".md")
            #doc.save(output_path)


            parser = Parser(pdf_name)
            parser.extract()
            piles = parser.parse()

            syntax = UrbanSyntax()

            print(folder_path)
            
            writer = Writer()
            writer.set_syntax(syntax)
            writer.set_mode('simple')
            writer.set_title(pdf_name_without_extension)
            writer.write(piles, folder_path)

            st.success(pdf_name + " successfully converted.")
            




def main():
    #load_dotenv() 
    st.set_page_config(page_title="Convert PDF to Markdown", page_icon=":books:")
    #st.write(css, unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files= True)
        
        if st.button("Convert"):
            with st.spinner("Converting PDF to Markdown..."):
                control_PDF(pdf_docs)
                convert_PDF(pdf_docs)


if __name__ == '__main__':
    main()