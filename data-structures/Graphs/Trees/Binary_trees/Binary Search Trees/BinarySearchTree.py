class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

class BST:
    def __init__(self, values):
        self.root = None

        for elem in values:
            self.insert(elem)

    def insert(self, new_elem):
        self.insert_helper(self.root, new_elem)

    def insert_helper(self, current, new_elem):
        if current < new_elem:
            if current.right:
                self.insert_helper(current.right, new_elem)
            else:
                current.right = Node(new_elem)

        elif current > new_elem:
            if current.left:
                self.insert_helper(current.left, new_elem)
            else:
                current.left = Node(new_elem)

        else:
            current.val = new_elem

    # def print_inorder(self, current=self.root):
    #     if current:
    #         self.print_inorder(current.left)
    #         print(current.val)
    #         self.print_inorder(current.right)


if __name__ == "__main__":
    new_bst = BST([1,9,2,8,3,7,4,6,5])
    new_bst.print_inorder()
