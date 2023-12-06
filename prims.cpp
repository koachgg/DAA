// #include <iostream>
// #include <vector>
// #include <climits>

// using namespace std;

// int minKey(const vector<int> &key, const vector<bool> &includedInMST, int V) {
//     int min = INT_MAX, minIndex;
//     for (int v = 0; v < V; v++) {
//         if (!includedInMST[v] && key[v] < min) {
//             min = key[v];
//             minIndex = v;
//         }
//     }
//     return minIndex;
// }

// void printMST(const vector<int> &parent, const vector<vector<int>> &graph) {
//     cout << "Edge \tWeight\n";
//     for (int i = 1; i < graph.size(); i++) {
//         cout << parent[i] << " - " << i << " \t" << graph[i][parent[i]] << endl;
//     }
// }

// void primMST(const vector<vector<int>> &graph) {
//     int V = graph.size();
//     vector<int> parent(V);
//     vector<int> key(V, INT_MAX);
//     vector<bool> includedInMST(V, false);

//     key[0] = 0;
//     parent[0] = -1;

//     for (int i = 0; i < V - 1; i++) {
//         int u = minKey(key, includedInMST, V);
//         includedInMST[u] = true;

//         for (int v = 0; v < V; v++) {
//             if (graph[u][v] && !includedInMST[v] && graph[u][v] < key[v]) {
//                 parent[v] = u;
//                 key[v] = graph[u][v];
//             }
//         }
//     }

//     printMST(parent, graph);
// }

// int main() {
//     vector<vector<int>> graph = {
//         {0, 2, 0, 6, 0},
//         {2, 0, 3, 8, 5},
//         {0, 3, 0, 0, 7},
//         {6, 8, 0, 0, 9},
//         {0, 5, 7, 9, 0},
//     };

//     primMST(graph);

//     return 0;
// }
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minKey(const vector<int>& key, const vector<bool>& includedInMST, int V) {
    int min = INT_MAX, minIndex = -1;
    for (int v = 0; v < V; v++) {
        if (!includedInMST[v] && key[v] < min) {
            min = key[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void printMST(const vector<int>& parent, const vector<vector<int>>& graph) {
    cout << "Edge \tWeight\n";
    for (int i = 1; i < graph.size(); i++) {
        cout << parent[i] << " - " << i << " \t" << graph[i][parent[i]] << endl;
    }
}

void primMST(vector<vector<int>>& graph) {
    int V = graph.size();
    vector<int> parent(V);
    vector<int> key(V, INT_MAX);
    vector<bool> includedInMST(V, false);

    key[0] = 0;
    parent[0] = -1;

    for (int i = 0; i < V - 1; i++) {
        int u = minKey(key, includedInMST, V);
        includedInMST[u] = true;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !includedInMST[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    printMST(parent, graph);
}

int main() {
    int V;
    cout << "Enter the number of vertices: ";
    cin >> V;

    vector<vector<int>> graph(V, vector<int>(V));

    cout << "Enter the adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cin >> graph[i][j];
        }
    }

    primMST(graph);

    return 0;
}