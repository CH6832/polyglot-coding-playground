#include "topologicalSortOfDrag.h"

int main() {
    // Create a graph given in the diagram
    TopologicalSortOfDrag g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    std::cout << "Following is a Topological sort of the given graph: ";
    g.topologicalSort();

    return 0;
}
