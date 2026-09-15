class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)

node5 = Node(5)
node20 = Node(20)
node3 = Node(3)
node7 = Node(7)

root.left = node5
root.right = node20

node5.left = node3
node5.right = node7


# print(f"\t\t\t\troot: {root.data}")
# print(f"\t\tleft: {root.left.data}\t\t\t right: {root.right.data}")
#
# print(f"left: {root.left.left.data}\t\t right: {root.left.right.data}")


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        # insert into empty tree
        if self.root is None:
            self.root = new_node

            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                print("Data is already present")
                return

    def contains(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def show_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            self.show_tree(node.right, level + 1, "R-- ")
            print("    " + str(level) + prefix + str(node.data))
            self.show_tree(node.left, level + 1, "L-- ")

    def pre_order(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def find_min(self):
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.data


tree = BinarySearchTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(90)
#
# print(f"\t\t\t\troot: {tree.root.data}")
# print(f"\t\tleft: {tree.root.left.data}\t\t\t right: {tree.root.right.data}")
# print(f"left: {tree.root.left.left.data}\t\t right: {tree.root.left.right.data} \t\t\tRight: {tree.root.right.right.data}")
# print(f"\t\t\t\t\t")
#
# print(tree.contains(26))


tree.show_tree(tree.root)

tree.pre_order(tree.root)
print("\nmin")
print(tree.find_min())
