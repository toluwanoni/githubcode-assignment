#new practice on classes
class Employee:
    def __init__ (self,first,last,payment):
        self.first = first
        self.last = last
        self.payment = payment 

    def payroll(self):
      print(f'The first staff to be paid is {self.first} {self.last},and the amount is {self.payment}')
    

staff1 =Employee ('olafioye','tolu',100000)
staff2 = Employee('salami','ganiyat',700000)

print(staff1.payroll())
print(staff2.payroll())
