from docx import Document
from sys import stdin
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, Inches
def n2():
    a = stdin.read().split("\n")
    d = Document()

    h = d.add_paragraph()
    h.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
    h = h.add_run(a[0])
    h.font.name = "Arial"
    h.font.italic = True
    h.font.size = Pt(11)

    a = a[1:]
    for i in range(len(a)-2):
        t = d.add_paragraph()
        t.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        t.paragraph_format.first_line_indent = Inches(0.5)
        t = t.add_run(a[i])
        t.font.name = "Times New Roman"
        t.font.size = Pt(12)

    e1 = d.add_paragraph()
    e1.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    e1 = e1.add_run(a[-2])
    e2 = d.add_paragraph()
    e2.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    e2 = e2.add_run(a[-1])
    e2.font.bold = True

    d.save("letter.docx")

def n1():
    a = stdin.read().split()
    d = Document()
    h = d.add_heading("Blood test", level=0)
    h.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    t = d.add_table(len(a) + 1, 3, style="Table Grid")
    head_t = t.rows[0].cells
    head = ["ingicator", "norm", "value"]
    for i in range(3):
        head_t[i].text = head[i]
        r = head_t[i].paragraphs[0].runs[0]
        r.font.bold = True
        head_t[i].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for i in range(1, len(a) + 1):
        s = t.rows[i].cells
        s[0].text = a[i - 1]
    d.save("analysis.docx")

n1()