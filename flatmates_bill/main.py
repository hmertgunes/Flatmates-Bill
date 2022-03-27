from PdfReport import PdfReport
from flat import Bill, Flatmates

the_bill = Bill(int(input("How much money is bill? ")), input("What period bill's is ?"))
the_flatmate = Flatmates(input("Who are you?"), int(input("How many days you stayed at home?")))
the_flatmate2 = Flatmates(input("Who are your flatmates?"), int(input("How many days he or she stayed at home?")))
print(f"You {the_flatmate.name} have to pay {the_flatmate.pays(the_bill, the_flatmate2)}$ "
      f"the flatmate {the_flatmate2.name} has to pay {the_flatmate2.pays(the_bill, the_flatmate)}$")

pdf_report = PdfReport(f"{the_bill.period}.pdf")
pdf_report.generate_pdf(bill=the_bill, flatmate1=the_flatmate, flatmate2=the_flatmate2)
