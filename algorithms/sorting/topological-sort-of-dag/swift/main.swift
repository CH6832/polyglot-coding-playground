// Topological Sort of DAG (Directed Acyclic Graph)
func topologicalSort(_ graph: [Int: [Int]]) -> [Int] {
    var visited: Set<Int> = []
    var stack: [Int] = []
    
    func dfs(_ node: Int) {
        visited.insert(node)
        
        if let neighbors = graph[node] {
            for neighbor in neighbors {
                if !visited.contains(neighbor) {
                    dfs(neighbor)
                }
            }
        }
        
        stack.append(node)
    }
    
    for node in graph.keys {
        if !visited.contains(node) {
            dfs(node)
        }
    }
    
    return stack.reversed()
}

// Example Usage
let graph: [Int: [Int]] = [
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
]

let sortedNodes = topologicalSort(graph)
print(sortedNodes) // Output: [1, 3, 2, 4, 5]
