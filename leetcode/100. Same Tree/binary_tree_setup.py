class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.val = 1
node1.left = node2
node1.right = node3
node2.val = 2
node2.left = node4
node2.right = node5
node3.val = 3
node3.left = node6
node3.right = None
node4.val = 4
node4.left = None
node4.right = None
node5.val = 5
node5.left = None
node5.right = None
node6.val = 6
node6.left = None
node6.right = None


def print_tree_dfs_recurse(node):
    if node is None:
        return
    print(node.val)
    print_tree_dfs_recurse(node.left)
    print_tree_dfs_recurse(node.right)


print("DFS Recursive:")
print_tree_dfs_recurse(node1)


def print_tree_dfs_iterate(node):
    stack = [node]
    while stack:
        current_node = stack.pop()
        if current_node is None:
            continue
        print(current_node.val)
        stack.append(current_node.left)
        stack.append(current_node.right)

        print(stack)


print("DFS Iterative:")
print_tree_dfs_iterate(node1)


def print_tree_bfs_iterate(node):
    from collections import deque

    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        if current_node is None:
            continue
        print(current_node.val)
        queue.append(current_node.left)
        queue.append(current_node.right)


print("BFS Iterative:")
print_tree_bfs_iterate(node1)


# Naturally, BFS cannot be implemented recursively, but we can simulate it using a queue and recursion. Here's a recursive approach to BFS:
def print_tree_bfs_recurse(node):
    def print_tree_bfs_recurse_helper(queue):
        if not queue:
            return

        node = queue.popleft()

        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)

        print_tree_bfs_recurse_helper(queue)

    from collections import deque

    print_tree_bfs_recurse_helper(deque([node]))


print("BFS Recursive:")
print_tree_bfs_recurse(node1)
