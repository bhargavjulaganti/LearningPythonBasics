from PyPDF2 import PdfFileMerger

#Create and instance of PdfFileMerger() class
merger = PdfFileMerger()

AbsolutePath = '/Users/bjulaganti/MyLearning/SamplePython/PlayingWithPdfs/'

#Create a list with file names
pdf_files = [AbsolutePath +'sample_page1.pdf', AbsolutePath + 'sample_page2.pdf']

#Iterate over the list of file names
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF
merger.write(AbsolutePath +"merged_2_pages.pdf")
merger.close()

# pdf-compressor --set-api-key secret_key_f0458390a38b2e5ae1adbe31b85a7e72_sQzgJ5033f661791a7a134c6e9dfa05e02a7b
# pdf-compressor --set-api-key project_public_51217323e4127e19f2f8eea56b5ae784_z6KR73fe1726c3c8243842b3c8e2bb33a0d87