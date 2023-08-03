import sampleData

def fraudulentGroups(sender, transactions):

    sorted_transactions = sorted(transactions, key=lambda x: x["date"])

    balances = {}
    balances[sender] = 1e19

    for transaction in sorted_transactions:
        sender = transaction["sender"]
        receiver = transaction["receiver"]
        amount = transaction["amount"]
        balances[receiver] = balances.get(receiver, 0) + min(balances.get(sender, 0), amount)

    balances[sender] = 0

    return balances

print(fraudulentGroups("3456789012", sampleData.transactions))

    

