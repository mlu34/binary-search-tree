import json
from typing import List

# DO NOT MODIFY THIS CLASS!
class Node():
    def  __init__(self,
                  key        = None,
                  keycount   = None,
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.keycount   = keycount
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key": node.key,
            "keycount": node.keycount,
            "leftchild": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

#---------------------------------------------------------------------------------------------------

# For the tree rooted at root and the key given:
# If the key is not in the tree, insert it with a keycount of 1.
# If the key is in the tree, increment its keycount.
def insert(root: Node, key: int) -> Node:
    if root == None:
        return Node(key, keycount = 1) 

    temp = root
    while temp:
        if key == temp.key:
            temp.keycount += 1
            return root
        elif key < temp.key:
            if temp.leftchild == None:
                temp.leftchild = Node(key, keycount = 1)
                return root
            else:
                temp = temp.leftchild
        else:
            if temp.rightchild == None:
                temp.rightchild = Node(key, keycount = 1)
                return root
            else:
                temp = temp.rightchild
    return root

# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If they keycount goes to 0, remove the key.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    # Root is empty, return root
    if root == None:
        return root
    
    # The key to delete is found
    if root.key == key:
        if root.keycount > 1:
            root.keycount -= 1
            return root
        else:
            # Case 1: the node we want to delete has no children
            if root.leftchild == None and root.rightchild == None:
                return None
            # Case 2: the node we want to delete only has a right child
            elif root.leftchild == None:
                return root.rightchild
            # Case 3: the node we want to delete only has a left child
            elif root.rightchild == None:
                return root.leftchild
            # Case 4: the node we want to delete has both children
            else:
                temp = root.rightchild
                while temp.leftchild:
                    temp = temp.leftchild
                root.key = temp.key
                root.keycount = temp.keycount
                # We want to delete the replacement key
                temp.keycount = 1
                root.rightchild = delete(root.rightchild, temp.key)
                return root
    # The key we want to delete is bigger than the root
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    # The key we want to delete is smaller than the root
    else:
       root.leftchild = delete(root.leftchild, key)
    return root

# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    if root == None:
        return(json.dumps([], indent = 2))
    elif root.key == search_key:
        return(json.dumps([root.key], indent = 2))
    else:
        arr = [root.key]
        while root != None:
            if search_key > root.key:
                root = root.rightchild
            elif search_key < root.key:
                root = root.leftchild
            if root == None:
                break
            arr.append(root.key)
            if search_key == root.key:
                break
        return(json.dumps(arr, indent = 2))

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def preorder(root: Node) -> str:
    return(json.dumps(preorderhelper(root), indent = 2))

def preorderhelper(root: Node):
    if root == None:
        return []
    arr = []
    arr.append(root.key)
    arr += preorderhelper(root.leftchild)
    arr += preorderhelper(root.rightchild)
    return arr

# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.
def inorder(root: Node) -> str:
    return(json.dumps(inorderhelper(root), indent = 2))

def inorderhelper(root: Node):
    if root == None:
        return []
    arr = []
    arr += inorderhelper(root.leftchild)
    arr.append(root.key)
    arr += inorderhelper(root.rightchild)
    return arr

# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    return(json.dumps(postorderhelper(root), indent = 2))

def postorderhelper(root: Node):
    if root == None:
        return []
    arr = []
    arr += postorderhelper(root.leftchild)
    arr += postorderhelper(root.rightchild)
    arr.append(root.key)
    return arr

# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.
def bft(root: Node) -> str:
    if root == None:
        return json.dumps([], indent = 2)
    q = []
    q.append(root)
    arr = []

    while len(q) > 0:
        temp = q.pop(0)
        if temp != None:
            arr.append(temp.key)
        if temp.leftchild != None:
            q.append(temp.leftchild)
        if temp.rightchild != None:
            q.append(temp.rightchild)
    return json.dumps(arr, indent = 2)