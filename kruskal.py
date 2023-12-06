def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)
    
    if rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    elif rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        rank[u_root] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n
    
    total_weight = 0
    selected_edges = []
    for u, v, weight in edges:
        u_root = find(parent, u)
        v_root = find(parent, v)
        
        if u_root != v_root:
            selected_edges.append((u, v, weight))
            total_weight += weight
            union(parent, rank, u_root, v_root)
            
    return total_weight, selected_edges

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))
    
    edges = []
    print("Enter the edges (u, v, weight):")
    for _ in range(m):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))
    
    total_weight, selected_edges = kruskal(n, edges)
    
    print("Selected edges:")
    for edge in selected_edges:
        print("({}, {}, {})".format(*edge))
    print("Total weight of the minimum spanning tree:", total_weight)