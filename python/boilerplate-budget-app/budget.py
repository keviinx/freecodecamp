class Category:

    # initialize
    def __init__(self, category):
        # set the category
        self.category = category
        # init the ledger as empty list
        self.ledger = []

    # accepts an amount and description.
    # If no description is given, it should default to an empty spring.
    # Should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    # similar to deposit method, but the amount passed in should be stored in the ledger as a negative number.
    # If there are not enough funds, nothing should be added to the ledger.
    # This method should return True if the withdrawal took place, and False otherwise.
    def withdraw(self, amount, description = ""):
        withdrawal_took_place = False
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            withdrawal_took_place = True
        return withdrawal_took_place

    # method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        # loop through to get the sum of amount
        return sum(i["amount"] for i in self.ledger)

    # method that accepts an amount and another budget category as arguments.
    # The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
    # The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
    # If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, budget_category):
        transfer_took_place = False
        # If amount is enough
        if self.check_funds(amount):
            # withdraw from self
            self.withdraw(amount, "Transfer to " + budget_category.name.capitalize())
            # deposit into another budget category
            budget_category.deposit(amount, "Transfer from " + self.name.capitalize())
            # set transfer took place to true
            transfer_took_place = True
        return transfer_took_place

    # method that accepts an amount as an argument.
    # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
    # This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        amount_is_lesser = False
        if amount > self.get_balance():
            amount_is_lesser = True
        return amount_is_lesser

    # budget object is printed based on README requirement
    def __str__(self):
        #TODO
        pass


def create_spend_chart(categories):
    #TODO
    pass