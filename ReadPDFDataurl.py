import io

import requests
from PyPDF2 import PdfFileReader

url = 'https://www.c2e2.com/content/dam/sitebuilder/rna/c2e2/2021/_docs/C2E2-Guests-2020.pdf.coredownload.052146785.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

reader = PdfFileReader(f)
contents = reader.getPage(0).extractText().split('\n')