import networkx as nx
import sampleData

def muleBridges(transactions):

    graph = nx.Graph()

    moneyTransfer = {}

    for transaction in transactions:
        sender = transaction["sender"]
        receiver = transaction["receiver"]
        amount = transaction["amount"]
        moneyTransfer[sender] = moneyTransfer.get(sender, 0) + amount
        graph.add_edge(sender, receiver)

    visited = set()
    parent = {}
    low = {}
    disc = {}
    ap = set()

    def dfs(node):
        nonlocal time
        child_count = 0
        visited.add(node)

        amountTransfer = moneyTransfer.get(node, 0)

        disc[node] = time
        low[node] = time
        time += 1

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                parent[neighbor] = node
                child_count += 1
                dfs(neighbor)

                low[node] = min(low[node], low[neighbor])

                if parent[node] is None and child_count > 1:
                    ap.add(tuple({node, amountTransfer}))
                if parent[node] is not None and low[neighbor] >= disc[node]:
                    ap.add(tuple({node, amountTransfer}))

            elif neighbor != parent[node]:
                low[node] = min(low[node], disc[neighbor])

    time = 0
    for node in graph.nodes:
        if node not in visited:
            parent[node] = None
            dfs(node)

    #returns a set of tuples, each which contains the node number and amount transferred
    return ap

print(muleBridges(sampleData.transactions))
