class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):# now our method has 2 parameters!
    	# we assign them accordingly
        self.name = name
        self.email = email_address
        self.account_balance = 0 # the account balance is set to $0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self,amount): #debits the account_balance for given amount
        self.account_balance -= amount

    def display_balance(self):
        print(f"{self.name}, Balance ${self.account_balance}")

    def transfer_money(self, other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_balance()
        other_user.display_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
drake = User('Drake Sanders', "drake@python.com")

guido.make_deposit(100) #guido deposits 100
guido.make_deposit(200) #guido deposits 200
guido.make_deposit(50)  #monty deposits 50
guido.make_withdrawal(200) #withdrawal for 200
guido.display_balance()

drake.make_deposit(500) #drake deposits 500
drake.make_deposit(500) #drake deposits 500
drake.make_withdrawal(100)
drake.make_withdrawal(200)
drake.display_balance() #displays 700

monty.make_deposit(300) #deposits 300
monty.make_withdrawal(100) #withdraws 100
monty.make_withdrawal(50) #withdraws 50
monty.make_withdrawal(50) #withdraws 50
monty.display_balance() #displays 100

drake.transfer_money(monty,200) #transfers 200 from drake to monty and displays new balance
#New balance for Drake should be 500, and 300 for monty