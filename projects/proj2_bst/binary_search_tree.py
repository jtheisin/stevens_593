
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  

class BinarySearchTree:
    def __init__(self,has_input=False):
        
        if has_input is False:
            num_lst = input("Please input a list of numbers separated by spaces: ")
            self.num_lst = num_lst.lstrip(' ').rstrip(' ').split(' ')
            self.num_lst = [int(x) for x in self.num_lst]            
        else:
            self.num_lst = [20, 10, 30, 5, 15, 25, 40]
        self.root = None

    def buildBinarySearchTree(self):
        for num in self.num_lst:
            self.insert(num)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = TreeNode(value)
                        current.left.parent = current 
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = TreeNode(value)
                        current.right.parent = current  
                        break
                    current = current.right
                    
    def insert_at(self, index, value):
        if index < 0:
            raise ValueError("Index should be non-negative")
        if index == 0:
            new_node = TreeNode(value)
            new_node.left = self.root
            if self.root:
                self.root.parent = new_node
            self.root = new_node
        else:
            inorder_result = self.inorderTraversal(prints=False)
            if index > len(inorder_result):
                raise ValueError("Index is out of range.")
            parent_value = inorder_result[index]
            parent = self.find_node(self.root, parent_value)
            new_node = TreeNode(value)
            if parent.left is None:
                parent.left = new_node
            else:
                new_node.left = parent.left
                parent.left.parent = new_node
                parent.left = new_node
            new_node.parent = parent

    def inorderTraversal(self,prints=True):
        result = []
        stack = []
        current = self.root
        out_str = ''
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            out_str+= str(current.value)+'; '
            result.append(current.value)
            current = current.right
        if prints is True:
            print(out_str)
        return result

    def find_node(self, current, value):
        if current is None:
            return None
        if current.value == value:
            return current
        if value < current.value:
            return self.find_node(current.left, value)
        else:
            return self.find_node(current.right, value)
        
        
    def delete(self, x):
        node_to_delete = self.find_node(self.root, x)
        if node_to_delete is None:
            print(f"{x} is not in the tree")
            return self.inorderTraversal()

        if node_to_delete.left is None and node_to_delete.right is None:
            self.delete_node(node_to_delete)
        elif node_to_delete.left is None or node_to_delete.right is None:
            if node_to_delete.left:
                child = node_to_delete.left
            else:
                node_to_delete.right
            if node_to_delete.parent is None:
                self.root = child
                child.parent = None
            else:
                child.parent = node_to_delete.parent
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child          
        else:
            successor = self.find_min(node_to_delete.right)
            node_to_delete.value = successor.value
            self.delete_node(successor)

        return self.inorderTraversal(prints=False)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node     
    
    def delete_node(self,node):
        if node.parent is None:
            self.root = None
        elif node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    

    def firstCommonAncestor(self, x, y, root=False):
        if root is False:
            root = self.root
        if root is None:
            return None
        if root.value == x or root.value == y:
            return root.value
        left_ancestor = self.firstCommonAncestor(x, y, root.left)
        right_ancestor = self.firstCommonAncestor(x, y, root.right)
        if left_ancestor and right_ancestor:
            return root.value
        if left_ancestor:
            return left_ancestor
        else:
            return right_ancestor

    def printTree(self, node=False, depth=0):
        if node is False:
            node = self.root
        if node is None:
            return
        if depth == 0:
            print("Binary Search Tree:")
        if node is not None:
            self.printTree(node.right, depth + 1)
            print("    |" * depth + "-- " + str(node.value))
            self.printTree(node.left, depth + 1)
