import math
class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None


def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.elem, end=' ')
    inorder(root.right)


def tree_construction(arr, i=1):
    if i >= len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p


class BTPrinter:

    # @staticmethod
    # def in_order_print(root):
    #     if root is None:
    #         print("null")
    #     else:
    #         BTPrinter.in_order_print_helper(root)
    #         print()

    # @staticmethod
    # def in_order_print_helper(root):
    #     if root is None:
    #         return
    #     BTPrinter.in_order_print_helper(root.left)
    #     print(root.elem, end=" ")
    #     BTPrinter.in_order_print_helper(root.right)

    @staticmethod
    def print_node(root):
        if root is None:
            print("null")
        else:
            max_level = BTPrinter.max_level(root)
            BTPrinter.print_node_internal([root], 1, max_level)

    @staticmethod
    def print_node_internal(nodes, level, max_level):
        if not nodes or BTPrinter.is_all_elements_null(nodes):
            return

        floor = max_level - level
        edge_lines = int(math.pow(2, max(floor - 1, 0)))
        first_spaces = int(math.pow(2, floor)) - 1
        between_spaces = int(math.pow(2, floor + 1)) - 1

        BTPrinter.print_whitespaces(first_spaces)

        new_nodes = []
        for node in nodes:
            if node is not None:
                print(node.elem, end="")
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            else:
                new_nodes.append(None)
                new_nodes.append(None)
                print(" ", end="")

            BTPrinter.print_whitespaces(between_spaces)

        print("")

        for i in range(1, edge_lines + 1):
            for j in range(len(nodes)):
                BTPrinter.print_whitespaces(first_spaces - i)
                if nodes[j] is None:
                    BTPrinter.print_whitespaces(
                        edge_lines + edge_lines + i + 1)
                    continue

                if nodes[j].left is not None:
                    elem_length = len(str(nodes[j].left.elem))
                    if elem_length == 1:
                        print("/", end="")
                    else:
                        print(" /", end="")
                else:
                    BTPrinter.print_whitespaces(1)

                BTPrinter.print_whitespaces(i + i - 1)

                if nodes[j].right is not None:
                    elem_length = len(str(nodes[j].right.elem))
                    if elem_length == 1:
                        print("\\", end="")
                    else:
                        print(" \\", end="")
                else:
                    BTPrinter.print_whitespaces(1)

                BTPrinter.print_whitespaces(edge_lines + edge_lines - i)

            print("")

        BTPrinter.print_node_internal(new_nodes, level + 1, max_level)

    @staticmethod
    def print_whitespaces(count):
        for _ in range(count):
            print(" ", end="")

    @staticmethod
    def max_level(node):
        if node is None:
            return 0
        return max(BTPrinter.max_level(node.left), BTPrinter.max_level(node.right)) + 1

    @staticmethod
    def is_all_elements_null(lst):
        for obj in lst:
            if obj is not None:
                return False
        return True
