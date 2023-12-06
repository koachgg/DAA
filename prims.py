def prim(graph):
    num_vertices = len(graph)
    selected_vertex = [False] * num_vertices
    num_edges = 0

    selected_vertex[0] = True

    while num_edges < num_vertices - 1:
        minimum = float('inf')
        a = 0
        b = 0
        for m in range(num_vertices):
            if selected_vertex[m]:
                for n in range(num_vertices):
                    if not selected_vertex[n] and graph[m][n]:
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
        print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))
        selected_vertex[b] = True
        num_edges += 1

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix:")
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        if len(row) != num_vertices:
            print("Error: Each row must have the number of vertices entries.")
            return
        graph.append(row)

    prim(graph)

if __name__ == "__main__":
    main()