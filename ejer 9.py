import networkx as nx
import itertools

def main():
    G = nx.Graph()

    planets = ['Tierra', 'Knowhere','Zen-Whober','Vomir','Titán','Nidavellir', 'planeta1', 'planeta2', 'planeta3', 'planeta4', 'planeta5', 'planeta6', 'planeta7']
    G.add_nodes_from(planets)

    planet_pairs = list(itertools.combinations(planets, 2))
    for i, pair in enumerate(planet_pairs):
        G.add_edge(pair[0], pair[1], weight=i)


    T = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
    print(T.edges())