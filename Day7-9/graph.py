# from collections import defaultdict
#
#
# class graph():
#
#     def __init__(self):
#         self.gr = defaultdict(list)
#
#     def addEdge(self, a, b):
#         self.gr[a].append(b)
#
#     def show(self, start):
#         queue = []
#         visited = [False] * len(self.gr)
#         queue.append(start)
#         while(queue):
#             el = queue.pop(0)
#             print(el, end=" ")
#             visited[el] = True
#             for i in self.gr[el]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True
#
#
# g = graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 4)
# g.addEdge(3, 4)
# g.addEdge(3, 5)
# g.addEdge(4, 5)
# g.addEdge(5, 4)
# g.addEdge(5, 3 )
#
# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
# g.show(0)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do inorder tree traversal


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val, end=" ")

        # now recur on right child
        printInorder(root.right)

    # A function to do postorder tree traversal


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val, end=" ")

    # A function to do preorder tree traversal


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" ")

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

    # Driver code


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
"Preorder traversal of binary tree is"
printPreorder(root)
print()
"\nInorder traversal of binary tree is"
printInorder(root)
print()
"\nPostorder traversal of binary tree is"
printPostorder(root)