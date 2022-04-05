class Category:

    def __init__(self, category):
        self.ledger = []
        self.balance = 0
        self.name = category
        self.withdrawals = 0  # for the bar chart function

    # append object to ledger list and add to balance
    def deposit(self, amount, description=''):
        dic = {"amount": amount, "description": description}
        self.balance += amount
        self.ledger.append(dic)

    # remove from balance if enough and append object to ledger
    def withdraw(self, amount, description=''):
        # check if there are enough funds
        if self.check_funds(amount) == True:
            withdrawal = -1 * amount
            self.balance -= amount
            self.withdrawals += withdrawal  # for bar chart function
            dic = {"amount": withdrawal, "description": description}
            self.ledger.append(dic)
            return True
        else:
            return False

    # get current balance of budget category
    def get_balance(self):
        return self.balance

    # transfer if enough funds
    def transfer(self, amount, category):
        destination = category.name
        if self.check_funds(amount) == True:
            self.withdraw(amount, ('Transfer to ' + destination))
            category.deposit(amount, ('Transfer from ' + self.name))
            return True
        else:
            return False

    # Returns True if enough funds, False if not
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    # String representation
    def __str__(self):
        title = self.name.center(30, '*')
        lines = []
        chart = ""
        total = str(self.balance)
        # loop through ledger, convert values into list of strings then join to make final string
        for entry in self.ledger:
            description = str(entry.get('description'))
            amount = (entry.get('amount'))
            rounded = "{:.2f}".format(amount)  # round to 2 decimal places
            line = description.ljust(23)[:23] + rounded.rjust(7) + '\n'
            lines.append(line)
        return title + '\n' + chart.join(lines) + 'Total: ' + total


def create_spend_chart(categories):
    # title at top that says "Percentage spent by category"
    # calculate percentage spent in each Category, (withdrawals only)
    total = 0
    percentages = []
    lines = []
    title = 'Percentage spent by category\n'
    rows = []

    longest = None
    total_withdrawals = 0
    for category in categories:
        total_withdrawals += category.withdrawals  # total spendinga
        # Determine longest word (for under the chart)
        cat = len(category.name)
        if longest is None or cat > longest:
            longest = cat
        # list of percentages rounded down to nearest 10
    for category in categories:
        percentage = int((((category.withdrawals / total_withdrawals) * 100) // 10) * 10)
        
        percentages.append(percentage)
    
    # make chart
    guide = 100
    omarks = []
    while guide >= 0:
        for percentage in percentages:
            if percentage < guide:
                omarks.append('   ')
            else:
                omarks.append(' o ')
        string = str(guide)
        chart = (string.rjust(3) + '|' + ''.join(omarks) + ' ' + '\n')
        lines.append(chart)
        omarks = []
        guide -= 10
    final_chart = ''.join(lines)

    # dashes at the bottom
    dashes = '    '
    length = len(chart)
    for x in range(length - 5):
        dashes += "-"

    # vertical words
    letters = []
    height = 0

    while height < longest:
        for category in categories:
            categ = category.name
            if len(categ) == longest and height == (longest - 1):
                letters.append(' ' + categ[height] + '  ')
            elif height < len(categ):
                letters.append(' ' + categ[height] + ' ')
            else:
                letters.append('   ')
        height += 1
        labels = ('    ' + ''.join(letters) + ' ' + '\n')
        rows.append(labels)
        letters = []

    label_chart = ''.join(rows)
    final_label_chart = label_chart[:-2]

    return title + final_chart + dashes + '\n' + final_label_chart