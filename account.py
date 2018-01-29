class Account:
    def __init__(self, starting_amount):
        self.__account_value = starting_amount

    def deposit(self, amount):
        self.__account_value += amount
    
    def withdraw(self, amount):
        self.__acount_value -= amount

    @property
    def current_value(self):
        return self.__account_value

    def transfer_to(self, acct, amount):
        self.withdraw(amount)
        acct.deposit(amount)