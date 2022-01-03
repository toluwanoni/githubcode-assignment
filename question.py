class wallet():
    def __init__(self,address,private_key):
        self.address = address
        self.privatee_key = private_key

    def get_balance(self):
        print(f"the balance of {self.address} is 10 ETH!")

my_wallet = wallet("232323", "xxxxxxx")
my_wallet.get_balance()    

a = 30
b = 40
print("a") if a < b else print("b")