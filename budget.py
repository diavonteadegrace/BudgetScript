class Income:
    def __init__(self):
        self.incomeD = 0
        #8th and the 23
        self.incomeJ = 0
        #every week
    def total(self):
        return sum ([

        self.incomeD * 2 + self.incomeJ * 4
    ])


class Bills:
    def __init__(self):
        self.car = 0
        self.car_insurance = 0
        self.phone = 0
        self.internet = 0
        self.credit1 = 0
        self.credit2 = 0
        self.credit3 = 0
        self.rentersins = 0
        self.utilities = 0
        self.rent = 0
        self.netflix = 0
        self.googleone = 0
        self.peacock = 0
        self.youtube = 10
        self.amazon = 0
        self.gas = 40 * 6
        self.gym = 0
        self.grocery = 0
        self.allowance = 150 * 4
        
    def total(self):
        return sum([
            self.car, self.car_insurance, self.phone, self.internet,
             self.credit1, self.credit2, self.credit3,
             self.rentersins, self.utilities, self.rent, self.netflix,
             self.googleone, self.grocery, self.allowance, self.gym, 
             self.peacock, self.gas, self.youtube, self.amazon
        ])


'''
    def debt(self):
        self.cardebt = 0
        self.discover_credit = 0
        self.star_credit = 0
        self.usbank_credit = 0
    def savings(self):
        self.totalsavings = 0
        self.weeklysavings
'''

i = Income()
print(f"Monthly income is: ${i.total()}")
b = Bills()
print(f"Monthly bills are: ${b.total()}")
left = i.total() - b.total()
print(f"After bills there is ${left} left over")
week = left / 4
print(f"An average of ${week} a week")


print("How much would you like in savings?")
savings = int(input())
#print(savings)
print("How much would you like towards credit cards? ")
credit = int(input())
#print(credit)
total_away = credit + savings
print(f"You need to put {total_away} away a week")
left_over = week - total_away
print(f"This leaves you {left_over} to play around with")
year_saving = savings * 52
year_credit = credit * 52
print(f"At your current credit card payements, you will pay off an additional {year_credit} in a year")
print(f"At your current savings, you will save {year_saving} in a year")


