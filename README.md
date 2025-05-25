# HTML to PDF Converter using Python (`pdfkit`) and `wkhtmltopdf` (Windows)

This guide shows you how to convert HTML to PDF using Python with `pdfkit` and `wkhtmltopdf` on Windows.

---
##  ✅ 
Create virtual environment Open terminal, go to your project folder 

Create virtual environment: python -m venv venv

Activate it (on Windows): venv\Scripts\activate 


## ✅ Step 2: Download and Install `wkhtmltopdf`

1. Go to the official download page:  
   👉 [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

2. Download the Windows installer, for example:  
   `wkhtmltox-0.12.6-1.msvc2015-win64.exe`

3. Run the installer and install `wkhtmltopdf`.  
   Default path is usually:  
   `C:\Program Files\wkhtmltopdf\bin`

---

### ➕ Add `wkhtmltopdf` to Windows PATH

1. Press `Win + R`, type `sysdm.cpl`, and hit **Enter**  
2. Go to the **Advanced** tab → click **Environment Variables**
3. Under **System variables**, find `Path` → click **Edit**
4. Click **New** and add this path:  


Restart your System:

5. Click OK on all dialogs to apply the changes

6. Open a new **Command Prompt** and run:

```bash
wkhtmltopdf --version


✅ Step 3: Install Python pdfkit
Run this in your terminal or command prompt:

pip install pdfkit


✅ Step 4: Sample Python Code

import pdfkit

html = """
<h1>Hello PDF</h1>
<p>This is a test HTML to PDF conversion on Windows.</p>
"""

# Specify the path to wkhtmltopdf if needed:
config = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

# Convert HTML string to PDF
pdfkit.from_string(html, 'output.pdf', configuration=config)

📝 This will create output.pdf in your current folder with the given HTML content.
