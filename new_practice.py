#new practice on classes
class Employee:
    def __init__ (self,first,last,payment):
        self.first = first
        self.last = last
        self.payment = payment 

    def emp_1(self):
      print(f'the first staff to be paid is {self.first}{self.last},and the amount is {self.payment}')
    
    def emp_2(self):
        print(f'the second staff to be paid {self.first}{self.last},and the amount is {self.payment} ')

staff1 =Employee ('olafioye','tolu',100000)
staff2 = Employee('salami','ganiyat',700000)

staff1.emp_1()
staff2.emp_2()
    
