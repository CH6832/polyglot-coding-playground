// Topological Sort of DAG (Directed Acyclic Graph)
use std::collections::{HashSet, HashMap};

fn topological_sort(graph: &HashMap<i32, Vec<i32>>) -> Vec<i32> {
    let mut visited: HashSet<i32> = HashSet::new();
    let mut stack: Vec<i32> = Vec::new();

    fn dfs(node: i32, graph: &HashMap<i32, Vec<i32>>, visited: &mut HashSet<i32>, stack: &mut Vec<i32>) {
        visited.insert(node);
        if let Some(neighbors) = graph.get(&node) {
            for &neighbor in neighbors {
                if !visited.contains(&neighbor) {
                    dfs(neighbor, graph, visited, stack);
                }
            }
        }
        stack.push(node);
    }

    for &node in graph.keys() {
        if !visited.contains(&node) {
            dfs(node, graph, &mut visited, &mut stack);
        }
    }

    stack.reverse();
    stack
}

// Example Usage
fn main() {
    let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
    graph.insert(1, vec![2, 3]);
    graph.insert(2, vec![4]);
    graph.insert(3, vec![4]);
    graph.insert(4, vec![5]);
    graph.insert(5, vec![]);

    let sorted_nodes = topological_sort(&graph);
    println!("{:?}", sorted_nodes); // Output: [1, 3, 2, 4, 5]
}
