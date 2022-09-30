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