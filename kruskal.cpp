#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

struct Edge {
    int u, v, weight;
    
    bool operator<(const Edge &other) const {
        return weight < other.weight;
    }
};

int find(vector<int> &parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

void kruskal(int n, vector<Edge> &edges) {
    sort(edges.begin(), edges.end());
    vector<int> parent(n);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
    
    int totalWeight = 0;
    for (Edge &edge : edges) {
        int uRoot = find(parent, edge.u);
        int vRoot = find(parent, edge.v);
        
        if (uRoot != vRoot) {
            cout << "Selected edge: (" << edge.u << ", " << edge.v << ", " << edge.weight << ")\n";
            totalWeight += edge.weight;
            parent[uRoot] = vRoot;
        }
    }
    cout << "Total weight of the minimum spanning tree: " << totalWeight << "\n";
}

int main() {
    int n, m;
    cout << "Enter the number of vertices and edges: ";
    cin >> n >> m;
    
    vector<Edge> edges(m);
    cout << "Enter the edges (u, v, weight):" << endl;
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
    }
    
    kruskal(n, edges);
    return 0;
}