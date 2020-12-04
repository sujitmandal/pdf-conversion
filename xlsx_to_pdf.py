import pandas as pd 
from fpdf import FPDF 

"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn
"""

data = pd.read_excel('data/data.xlsx')
data = data.drop(['Unnamed: 0'], axis = 1)
data.reset_index(drop=True, inplace=True)

info = []
data = str(data)
info.append(data)

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=20)
pdf.cell(200, 30, txt='Convert Xlsx To PDF', ln=1, align = 'C')


for j in range(len(info)):
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(200, 5, txt=info[j], align = '')
    
pdf.output('pdf/xlsx_to_pdf.pdf')    