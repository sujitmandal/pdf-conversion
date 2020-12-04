import json
from fpdf import FPDF

"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn
"""

with open('data/data.json') as a:
    data = json.load(a)

users = data.get('users')
numberOfUser = len(users)

main_data = []

while(numberOfUser != 0):
    main_data.append(users[numberOfUser - 1])
    numberOfUser -= 1

main_data.reverse()
keys = []
values = []
texts = []

for i in range(len(main_data)):
    user = main_data[i]

    for key, value in user.items():
        keys.append(key)
        values.append(value)

for info in range(len(keys)):
    text = keys[info] + ' ' + '=' + ' ' + str(values[info])
    texts.append(text)


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=20)
pdf.cell(200, 30, txt='Convert Json To PDF', ln=1, align = 'C')


for datas in range(len(texts)):
    pdf.set_font('Arial', size=10)
    pdf.multi_cell(200, 5, txt=texts[datas], align = '')

pdf.output('pdf/json_to_pdf_while_loop.pdf')    