#include <iostream>
#include <vector>

class DisjointSet {
private:
    std::vector<int> parent;
    std::vector<int> rank;

public:
    DisjointSet(int n) : parent(n), rank(n, 0) {
        // Initialize each element as a root with rank 0
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        // Find the root of the set containing element x
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    void unite(int x, int y) {
        // Union by rank
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY) return; // Already in the same set

        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }
};

int main() {
    DisjointSet ds(5);

    ds.unite(0, 2);
    ds.unite(4, 2);
    ds.unite(3, 1);

    std::cout << "Element 0 and 2 belong to the same set: " << (ds.find(0) == ds.find(2)) << std::endl;
    std::cout << "Element 0 and 3 belong to the same set: " << (ds.find(0) == ds.find(3)) << std::endl;

    return 0;
}
