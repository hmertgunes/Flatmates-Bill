from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template("BillFormPage.html", bill_form=bill_form)


class ResultPage(MethodView):

    def post(self):

        billform = BillForm(request.form)

        bill = flat.Bill(float(billform.amount.data), billform.period.data)
        f_1 = flat.Flatmates(billform.name1.data, float(billform.days_in_house1.data))
        f_2 = flat.Flatmates(billform.name2.data, float(billform.days_in_house2.data))

        return render_template("ResultPage.html", name1=f_1.name,
                               name2=f_2.name,
                               name1_pays=f_1.pays(bill, f_2),
                               name2_pays=f_2.pays(bill, f_1))


class BillForm(Form):
    amount = StringField(label="Bill Amount ", default=100)
    period = StringField(label="Bill Period ", default="Nisan 2022")
    name1 = StringField(label="Name", default="Mert")
    days_in_house1 = StringField(label="Days", default=15)
    name2 = StringField(label="Name", default="Eren")
    days_in_house2 = StringField(label="Days", default=15)
    button = SubmitField(label="Calculate Bills")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/result", view_func=ResultPage.as_view("result_page"))
app.run(debug=True)
