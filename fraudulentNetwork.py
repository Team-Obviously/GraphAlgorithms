import sampleData 
import queue

def detectFraudulentNetwork(transactions):

    sorted_transactions = sorted(transactions, key=lambda x: x["date"])
    print(sorted_transactions)

    balances = {}
    for transaction in sorted_transactions:
        sender = transaction["sender"]
        receiver = transaction["receiver"]
        amount = transaction["amount"]

        balances[sender] = balances.get(sender, 0) - amount
        balances[receiver] = balances.get(receiver, 0) + amount

    delta, sinkNode, amount = 0, 0, 0

    for account, balance in balances.items():
        delta = min(delta, balance)

    for i in balances:
        balances[i] -= delta
  
    adjacency_list = {}
    reversed_adjacency_list = {}

    for transaction in sorted_transactions:
        sender = transaction["sender"]
        receiver = transaction["receiver"]
        amount = transaction["amount"]

        if receiver in reversed_adjacency_list:
            reversed_adjacency_list[receiver].append(sender)
        else:
            reversed_adjacency_list[receiver] = [sender]

        if sender in adjacency_list:
            adjacency_list[sender].append([receiver, amount])
        else:
            adjacency_list[sender] = [[receiver, amount]]

    for account, balance in balances.items():
        if(account in reversed_adjacency_list):
            if(amount <= balance * len(reversed_adjacency_list[account])):
                amount = balance * len(reversed_adjacency_list[account])
                sinkNode = account
            
    edges = []
    q = queue.Queue()
    q.put(sinkNode)
    visited = [sinkNode]

    while(not q.empty()):
          front = q.get()

          if(front in reversed_adjacency_list):
              for x in reversed_adjacency_list[front]:
                  if(x not in visited):
                    visited.append(x)
                    q.put(x)
                    
                    if(x in adjacency_list):
                        for y, z in adjacency_list[x]:
                            if(y in visited):
                                edges.append([x, y, z])
    #returns a list of edges
    return edges

print(detectFraudulentNetwork(sampleData.transactions))
