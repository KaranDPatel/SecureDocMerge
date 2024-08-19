**Secure PDF Merger Using Python**

**Overview**

This project provides a secure and efficient way to merge multiple PDF files into a single document using Python. By leveraging the PyPDF2 library, you can combine PDF files directly from your local system without relying on third-party tools, ensuring the security and privacy of your documents.

**Features**

Local PDF Merging: Merge multiple PDF files stored locally into a single PDF document.

Secure Processing: Avoid using online third-party services to maintain the confidentiality of your files.

Simple Integration: Easy to integrate into any Python project or use as a standalone script.

Cross-Platform: Works on any platform where Python and PyPDF2 are supported.

**Prerequisites**

Python 3.x installed on your system.

Required Python packages: PyPDF2.

**Installation**

Clone the Repository:

sh
Copy code
git clone url
cd secure-pdf-merger


**Install Required Python Packages:**

sh
Copy code
pip install PyPDF2
Usage

Place Your PDFs:

Put all the PDF files you want to merge into the pdf directory (or modify the path variable in the script to point to your PDF directory).

Run the Script:

sh
Copy code
python merge_pdfs.py
Merged Output:


The script will combine all the PDFs in the specified directory and output a single merged PDF file named MergePdfFiles.pdf in the script's directory.

File Structure

graphql
Copy code
secure-pdf-merger/

│

├── merge_pdfs.py           # Main script for merging PDF files

├── pdf/                    # Directory containing PDFs to merge

├── README.md               # This readme file

└── requirements.txt        # List of Python dependencies (if applicable)

**Customization**

Output File Name: Modify the fout variable in the script to change the name of the merged PDF file.

PDF Directory: Change the path variable to specify a different directory for your PDF files.

Benefits

Security: By using this local script, you avoid potential data breaches that can occur when using online PDF merging tools.

Control: You have complete control over the merging process, with the ability to customize and extend the functionality as needed.
