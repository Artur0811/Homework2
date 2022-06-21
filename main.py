from docx import Document
from sys import stdin
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
a = stdin.read().split()
d = Document()
h = d.add_heading("Blood test", level=0)
h.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
t = d.add_table(len(a)+1, 3, style= "Table Grid")
head_t = t.rows[0].cells
head = ["ingicator", "norm", "value"]
for i in range(3):
    head_t[i].text = head[i]
    r = head_t[i].paragraphs[0].runs[0]
    r.font.bold = True
    head_t[i].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
for i in range(1, len(a)+1):
    s = t.rows[i].cells
    s[0].text = a[i-1]
d.save("analysis.docx")