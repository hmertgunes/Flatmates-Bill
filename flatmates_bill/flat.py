class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        return (self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)) * bill.amount
