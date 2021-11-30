class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):# now our method has 2 parameters!
    	# we assign them accordingly
        self.name = name
        self.email = email_address
        self.account_balance = 0 # the account balance is set to $0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self,amount): #debits the account_balance for given amount
        self.account_balance -= amount
        return self

    def display_balance(self):
        print(f"{self.name}, Balance ${self.account_balance}")

    def transfer_money(self, other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_balance()
        other_user.display_balance()
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
drake = User('Drake Sanders', "drake@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(200).display_balance()

drake.make_deposit(500).make_deposit(500).make_withdrawal(100).make_withdrawal(200).display_balance()

monty.make_deposit(300).make_withdrawal(100).make_withdrawal(50).display_balance()

drake.transfer_money(monty,200).transfer_money(guido,50)