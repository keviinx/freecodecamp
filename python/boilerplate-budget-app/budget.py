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
    def withdraw(amount, description = ""):
        withdrawal_took_place = False
        return withdrawal_took_place

    # method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance():
        # TODO
        pass

    # method that accepts an amount and another budget category as arguments.
    # The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
    # The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
    # If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer():
        # TODO
        pass

    # method that accepts an amount as an argument.
    # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
    # This method should be used by both the withdraw method and transfer method.
    def check_funds():
        # TODO
        pass

def create_spend_chart(categories):
    #TODO
    pass