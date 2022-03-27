import os
import webbrowser
from fpdf import FPDF


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, bill, flatmate1, flatmate2):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # ADD ICON
        pdf.image("files/house.png", w=30, h=30)
        # INSERT TITLE
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)
        # INSERT PERIOD AND VALUE
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=100, h=40, txt="Period:", align="C")
        pdf.cell(w=300, h=40, txt=bill.period, align="C", ln=1)
        # INSERT FLATMATES AND THEIR BILL'S
        pdf.set_font(family="Times", size=16, style="I")
        pdf.cell(w=100, h=25, txt=flatmate1.name, align="C", ln=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, other_flatmate=flatmate2))), align="C", ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, align="C", ln=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, other_flatmate=flatmate1))), align="C")

        os.chdir("files")

        pdf.output(self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))
