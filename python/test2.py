import qrcode
img = qrcode.make('https://www.google.com')
type(img) 
img.save('test.png')

import random
from fpdf import FPDF
import qrcode
img = qrcode.make('https://www.google.com')
type(img) 
img.save('test.png')

pdf = FPDF()

a1 = random.randint(1,9)
a2 = a3 = a1
while a2 == a1:
    a2 = random.randint(1,9)
while a3 == a1 or a3 == a2:
    a3 = random.randint(1,9)

b1 = random.randint(10,19)
b2 = b3 = b1
while b2 == b1:
    b2 = random.randint(10,19)
while b3 == b1 or b3 == b2:
    b3 = random.randint(10,19)

c1 = random.randint(20,29)
c2 = c3 = c1
while c2 == c1:
    c2 = random.randint(20,29)
while c3 == c1 or c3 == c2:
    c3 = random.randint(20,29)


print(a1, a2, a3, b1, b2, b3, c1, c2, c3,)

row1 = [a1, a2, a3]
row2 = [b1, b2, b3]
row3 = [c1, c2, c3]

pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = row1, ln = True, align = 'C')

pdf.cell(200, 10, txt = row2, ln = True, align = 'C')

pdf.cell(200, 10, txt = row3, ln = True, align = 'C')

pdf.output("test.pdf")


# print(n1, n2, n3, n4, n5, n6, n7, n8, n9)