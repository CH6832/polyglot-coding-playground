const std = @import("std");
const mem = std.mem;

const Node = struct {
    left: ?*Node,
    right: ?*Node,
    val: i32,
};

pub fn initNode(val: i32) Node {
    return Node{
        .left = null,
        .right = null,
        .val = val,
    };
}

pub fn findLCA(root: ?*Node, n1: i32, n2: i32) !i32 {
    if (root == null) {
        return Error.InvalidNode;
    }

    var path1: [1000]i32 = undefined;
    var path2: [1000]i32 = undefined;
    var path1_len: usize = 0;
    var path2_len: usize = 0;

    // Find paths from root to n1 and root to n2.
    if (!findPath(root, &path1, &path1_len, n1) or
        !findPath(root, &path2, &path2_len, n2)) {
        return Error.InvalidNode;
    }

    // Compare the paths to get the first different value
    var i: usize = 0;
    while (i < path1_len and i < path2_len) {
        if (path1[i] != path2[i]) {
            break;
        }
        i += 1;
    }
    return path1[i - 1];
}

pub fn findPath(root: ?*Node, path: &[*]i32, path_len: &usize, k: i32) bool {
    if (root == null) {
        return false;
    }

    path[*path_len] = root.*.val;
    *path_len += 1;

    // Check if the current node is the target node
    if (root.*.val == k) {
        return true;
    }

    // Check if the target node is found in the left or right subtree
    if ((root.*.left != null and findPath(root.*.left, path, path_len, k)) or
        (root.*.right != null and findPath(root.*.right, path, path_len, k))) {
        return true;
    }

    // If the target node is not found in the subtree rooted with root, remove the current node from the path and return False
    *path_len -= 1;
    return false;
}

const Error = enum {
    InvalidNode,
};

pub fn main() void {
    var root: Node = initNode(1);
    root.left = &Node{ .val = 2 };
    root.right = &Node{ .val = 3 };
    root.left.*.left = &Node{ .val = 4 };
    root.left.*.right = &Node{ .val = 5 };
    root.right.*.left = &Node{ .val = 6 };
    root.right.*.right = &Node{ .val = 7 };

    // Example call to find the lowest common ancestor of nodes 4 and 6
    const lca = try findLCA(&root, 4, 6);
    if (lca != Error.InvalidNode) {
        std.debug.print("Lowest Common Ancestor of 4 and 6: {}\n", .{lca});
    } else {
        std.debug.print("Invalid Node\n", .{});
    }
}
