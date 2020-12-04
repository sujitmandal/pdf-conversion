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

user1 = []
user2 = []
user3 = []
user4 = []
user5 = []

for i in range(len(users)):
    if i == 0:
        user1.append(users[i])
    elif i == 1:
        user2.append(users[i])
    elif i == 2:
        user3.append(users[i])
    elif i == 3:
        user4.append(users[i])
    elif i == 4:
        user5.append(users[i])
 
def keyvalue(lists):
    user = lists[0]
    keys = []
    values = []

    for key, value in user.items():
        keys.append(key)
        values.append(value)

    texts = []
    for i in range(len(keys)):
        text = keys[i] + ' ' + '=' + ' ' + str(values[i])
        texts.append(text)
    return(texts)

list1 = keyvalue(user1)
list2 = keyvalue(user2)
list3 = keyvalue(user3)
list4 = keyvalue(user4)
list5 = keyvalue(user5)


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', size=20)
pdf.cell(200, 30, txt='Convert Json To PDF', ln=1, align = 'C')

def pdfLine(info):
    for j in range(len(info)):
        pdf.set_font('Arial', size=10)
        pdf.cell(200, 5, txt=info[j], ln=1, align = '')
    pdf.cell(200, 5, txt='', ln=1)

pdfLine(list1)
pdfLine(list2)
pdfLine(list3)
pdfLine(list4)
pdfLine(list5)

pdf.output('pdf/json_to_pdf.pdf')    