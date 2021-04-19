class Category:

    # initialize
    def __init__(self, category):
        # set the category
        self.category = category
        # init the ledger as empty list
        self.ledger = []

    # accepts an amount and description.
    # If no description is given, it should default to an empty spring.
    def deposit(self, amount, description = ""):
        # Should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.append({"amount": amount, "description": description})

    # similar to deposit method, but the amount passed in should be stored in the ledger as a negative number.
    def withdraw(self, amount, description = ""):
        # If there are not enough funds, nothing should be added to the ledger.
        withdrawal_took_place = False
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            # This method should return True if the withdrawal took place, and False otherwise.
            withdrawal_took_place = True
        return withdrawal_took_place

    # method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        # loop through to get the sum of amount
        return sum(i["amount"] for i in self.ledger)

    # method that accepts an amount and another budget category as arguments.
    def transfer(self, amount, budget_category):
        transfer_took_place = False
        # If there are not enough funds, nothing should be added to either ledgers.
        if self.check_funds(amount):
            # The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
            self.withdraw(amount, "Transfer to " + budget_category.category.capitalize())
            # The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
            budget_category.deposit(amount, "Transfer from " + self.category.capitalize())
            # This method should return True if the transfer took place, and False otherwise.
            transfer_took_place = True
        return transfer_took_place

    # method that accepts an amount as an argument.
    # This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        amount_is_lesser = True
        if amount > self.get_balance():
            amount_is_lesser = False
        return amount_is_lesser

    # budget object is printed based on README requirement
    def __str__(self):
        # A title line of 30 characters where the name of the category is centered in a line of `*` characters.
        output = self.category.center(30, "*") + "\n"
        # A list of the items in the ledger. 
        # Each line should show the description and amount. 
        for item in self.ledger:
            # The first 23 characters of the description should be displayed, then the amount. 
            description = item["description"][:23].ljust(23)
            # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
            amount = f'{item["amount"]:7.2f}'
            output += f'{description + amount}\n'
        output += f'Total: {self.get_balance()}'
        return output

# Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. 
# It should return a string that is a bar chart.

# The chart should show the percentage spent in each category passed in to the function. 
# The percentage spent should be calculated only with withdrawals and not with deposits. 
# Down the left side of the chart should be labels 0 - 100. 
# The "bars" in the bar chart should be made out of the "o" character. 
# The height of each bar should be rounded down to the nearest 10. 
# The horizontal line below the bars should go two spaces past the final bar. 
# Each category name should be written vertically below the bar. 
# There should be a title at the top that says "Percentage spent by category".
def create_spend_chart(categories):
    #TODO
    pass