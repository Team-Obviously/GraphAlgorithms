import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import sampleData

def sourceToSink(source, sink, transactions):
    G = nx.DiGraph()

    for transaction in transactions:
        sender = transaction["sender"]
        receiver = transaction["receiver"]
        amount = transaction["amount"]
        G.add_edge(sender, receiver, capacity=amount)

    flow_value, flow_dict = nx.maximum_flow(G, source, sink)

    return flow_value

print(sourceToSink("3456789012", "0987654321", sampleData.transactions))

