import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (наприклад, зупинки)
nodes = ["Центральна станція", "Парк", "Університет", "Торгівельний центр", "Аеропорт"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами (наприклад, маршрути з відстанями)
edges = [
    ("Центральна станція", "Парк", 5),
    ("Центральна станція", "Університет", 3),
    ("Центральна станція", "Торгівельний центр", 7),
    ("Парк", "Університет", 2),
    ("Університет", "Торгівельний центр", 1),
    ("Торгівельний центр", "Аеропорт", 8),
    ("Парк", "Аеропорт", 10)
]
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Транспортна мережа Дніпра")
plt.show()

# Завдання 2: DFS та BFS
dfs_path = list(nx.dfs_edges(G, source="Центральна станція"))
bfs_path = list(nx.bfs_edges(G, source="Центральна станція"))

print("DFS Шлях:", dfs_path)
print("BFS Шлях:", bfs_path)

# Завдання 3: Алгоритм Дейкстри
dijkstra_path = nx.dijkstra_path(G, source="Центральна станція", target="Аеропорт")
print("Шлях за алгоритмом Дейкстри:", dijkstra_path)


# Функція для візуалізації шляхів
def draw_path(G, path, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    edge_colors = ['red' if (u, v) in path or (v, u) in path else 'black' for u, v in G.edges()]
    nx.draw(G, pos, edge_color=edge_colors, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

    plt.title(title)
    plt.show()


# Візуалізація шляхів DFS, BFS та Дейкстри
draw_path(G, dfs_path, "DFS Шлях від Центральної станції")
draw_path(G, bfs_path, "BFS Шлях від Центральної станції")
draw_path(G, [(dijkstra_path[i], dijkstra_path[i + 1]) for i in range(len(dijkstra_path) - 1)],
          "Шлях за алгоритмом Дейкстри від Центральної станції до Аеропорту")