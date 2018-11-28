class BankAccount(object):
   
#the initial balance is zero by default
    def __init__(self):
        self._balance = None

    def error_if_closed(self):       
#Raise a ValueError if the account is already closed.
        
        if self._balance is None:
            raise ValueError("Cannot perform operations on a closed account!")

    def get_balance(self) -> int:       
#Get the curreny balance of the account.
             
        self.error_if_closed()
        return self._balance

    def open(self):
        
#Open the account and initialize the balance.
        
        self._balance = 0

    def deposit(self, amount: int):
#Deposit amount into account. Raises ValueError on negative amounts.
        
        self.error_if_closed()
        if amount < 0:
            raise ValueError("Cannot make negative deposits!")
        self._balance += amount

    def withdraw(self, amount):
        
#Withdraw amount from account. Raises ValueError on negative or overdraft withdrawls.
        
        self.error_if_closed()
        if amount < 0:
            raise ValueError("Cannot make negative withdrawls!")
        elif amount > self._balance:
            raise ValueError("Cannot make withdrawls exceeding balance!")
        self._balance -= amount

    def close(self):
#Close the account.
       
        self._balance = None
