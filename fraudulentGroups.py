import sampleData
import networkx as nx
import community

def fraudulentGroups(transactions):

    G = nx.Graph()

    for transaction in transactions:
        G.add_edge(transaction['sender'], transaction['receiver'])
            
    partition = community.best_partition(G)

    #this is a dictionary which returns which community each node belongs to 
    #key is account number, value is community number
    return partition

print(fraudulentGroups(sampleData.transactions))