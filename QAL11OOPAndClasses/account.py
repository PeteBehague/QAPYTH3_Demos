class Account:
    numCreated = 0

    def __init__(self, initial):
        self._balance = initial
        Account.numCreated += 1


    def deposit(self, amt):
        self._balance += amt
        return


    def withdraw(self, amt):
        self._balance -= amt
        return


    def getbalance(self):
        return self._balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amt):
        if amt < 0:
            return
        self._balance = amt

    #balance = property(get_balance, set_balance)


    def __str__(self):
        return f"The current balance is {self._balance}"
