# username - strull
# id1      - 318731437
# name2    - Ofir Strull
# id2      - 206590879
# name1    - Noy Netanel
"""A class represnting a node in an AVL tree"""

"""
Checks if the node is real and not aa virtual node or None
"""


def is_real_node(node):
    return node is not None and node.is_real_node()


"""
This method creates a subtree from a node
"""


def tree_from_node(node):
    tree = AVLTree()
    tree.root = node
    node.set_parent(None)
    return tree


class AVLNode(object):

    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent
        self.size = 0
        if parent is None:
            self.height = 0
        else:
            self.height = parent.get_height() + 1
        self.height = 0
        if key is not None:
            self.left = AVLNode(None, None, self)
            self.right = AVLNode(None, None, self)
            self.size = 1
        else:
            self.left = None
            self.right = None
            self.size = 0
            self.height = -1  # virtual node is of height -1

    """returns the key of the node

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value of the node

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        if not self.is_real_node():
            return None
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        if not self.is_real_node():
            return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        if self is None:
            return -1
        return self.height

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self):
        return self.size

    def get_is_right(self):
        if self.parent is not None:
            return self.parent.get_right() is self

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """sets the size of node

    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.key is not None

    """
        get balance of a node: height of the left son - height of the right son
    """

    def get_balance(self):
        if not self.is_real_node():
            return -1
        if self.get_left() is None:
            return self.get_right().get_height()
        if self.get_right() is None:
            return self.get_left().get_height()
        return self.get_left().get_height() - self.get_right().get_height()

    def is_leaf(self):
        return not self.is_real_node()

    """
        set new_child instead of the old_child
    """

    def set_child(self, old_child, new_child):
        if old_child is self.right:
            self.set_right(new_child)
        elif old_child is self.left:
            self.set_left(new_child)

    """
        return the number of children of the current node
    """

    def get_children_count(self):
        res = 0
        if is_real_node(self.get_right()):
            res += 1
        if is_real_node(self.get_left()):
            res += 1
        return res

    """
        replace the self node with other - including all the pointers.
        The method updates also the size and the height fields 
    """

    def replace_with(self, other):
        if self.get_parent() is not None:
            self.get_parent().set_child(self, other)
        other.set_parent(self.get_parent())

        # if is_real_node(self.get_right()):
        self.get_right().set_parent(other)
        other.set_child(other.get_right(), self.get_right())

        # if is_real_node(self.get_left()):
        self.get_left().set_parent(other)
        other.set_child(other.get_left(), self.get_left())

        other.set_size(self.get_size())
        other.set_height(self.get_height())

    """
        get the sibling of self.
    """

    def get_sibling(self):
        parent = self.parent
        if parent is None:
            return None
        if parent.get_right() is self:
            return parent.get_left()
        return parent.get_right()


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None

    # add your fields here

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    run time complexity- O(logn)
    """

    def search(self, key):
        if self.root is None:
            return None
        node = self.root
        # A simple binary search tree method
        while node.get_key() is not None:
            if key == node.key:
                return node
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    run time complexity- O(logn)
    """

    def insert(self, key, val):
        # If we are inserting the first node
        if not is_real_node(self.root):
            self.root = AVLNode(key=key, value=val, parent=None)
        else:
            # Insert the node as a BST
            inserted = self.bst_insert_rec(node=self.root, key=key, val=val)
            # Update the heights
            heights_updated_count = self.update_parents_height_after_insert(parent=inserted.get_parent(),
                                                                            updated_child_node=inserted)
            # Rotate the tree and return the total work
            return self.manage_rotation_after_insert(inserted, heights_updated_count)

    """ manage the rotations after insert a node. 
    run time complexity- O(logn)
    """

    # def manage_rotation_after_insert(self, inserted, height_updated_count):


    def manage_rotation_after_insert(self, inserted, height_updated_count):
        loop_counter = height_updated_count
        parent = inserted.get_parent()
        balance_actions = 0
        # algorithm exactly as pseudo code in presentation
        while parent is not None:
            balance_actions += 1
            loop_counter -= 1
            balance = parent.get_balance()
            if abs(balance) < 2 and loop_counter == 0:
                return balance_actions+1
            elif abs(balance) < 2 and loop_counter > 0:
                parent = parent.get_parent()
            else:  # balance ==2
                criminal_before_rotation = parent
                criminal_parent_before_rotation = parent.get_parent()
                balance_actions += self.rotate_after_action(criminal=parent)
                node_to_update_height = criminal_parent_before_rotation
                # fix all heights starting from original criminal's parent
                for i in range(height_updated_count - criminal_before_rotation.get_height() - 2):
                    if node_to_update_height is None:
                        break
                    node_to_update_height.set_height(node_to_update_height.get_height() - 1)
                    node_to_update_height = node_to_update_height.get_parent()
                return balance_actions
        return balance_actions

    """
    calls the rotations functions according to the cases we saw in class. 
    """

    def rotate_after_action(self, criminal):  # rotate after insertion or deletion
        if criminal.get_balance() == -2:
            right_child_balance = criminal.get_right().get_balance()
            # notice that after insertion the bf of son can't be 0, only after deletion
            if right_child_balance == -1 or right_child_balance == 0:
                self.left_rotation(criminal)
                return 1
            elif right_child_balance == 1:
                self.right_left_rotation(criminal)
                return 2
        elif criminal.get_balance() == 2:
            left_child_balance = criminal.get_left().get_balance()
            if left_child_balance == -1:
                self.left_right_rotation(criminal)
                return 2
            # notice that after insertion the bf of son can't be 0, only after deletion
            elif left_child_balance == 1 or left_child_balance == 0:
                self.right_rotation(criminal)
                return 1
        return 0

    """left rotation- same as in presentation"""

    def left_rotation(self, criminal):
        parent = criminal.get_parent()
        criminal_replacer = criminal.get_right()
        # update the criminal's parent child pointer
        if parent is not None:
            parent.set_child(criminal, criminal_replacer)
        else:
            self.root = criminal_replacer
        # update the criminal's parent
        criminal.set_parent(criminal_replacer)
        #
        criminal.set_right(criminal_replacer.get_left())
        criminal_replacer.get_left().set_parent(criminal)
        # update the replacer of the criminal
        criminal_replacer.set_left(criminal)
        criminal_replacer.set_parent(parent)
        # fix heights
        criminal.set_height(max(criminal.get_right().get_height(), criminal.get_left().get_height()) + 1)
        criminal_replacer.set_height(
            max(criminal_replacer.get_right().get_height(), criminal_replacer.get_left().get_height()) + 1)
        # fix sizes
        criminal_original_size = criminal.get_size()
        criminal.set_size(criminal.get_size() - 1 - criminal_replacer.get_right().get_size())
        criminal_replacer.set_size(criminal_original_size)

    """right rotation- same as in presentation"""

    def right_rotation(self, criminal):
        parent = criminal.get_parent()
        criminal_replacer = criminal.get_left()
        # update the criminal's parent child pointer
        if parent is not None:
            parent.set_child(criminal, criminal_replacer)
        else:
            self.root = criminal_replacer
        # update the criminal's parent
        criminal.set_parent(criminal_replacer)
        #
        criminal.set_left(criminal_replacer.get_right())
        criminal_replacer.get_right().set_parent(criminal)
        # update the replacer of the criminal
        criminal_replacer.set_right(criminal)
        criminal_replacer.set_parent(parent)
        # fix heights
        criminal.set_height(max(criminal.get_right().get_height(), criminal.get_left().get_height()) + 1)
        criminal_replacer.set_height(
            max(criminal_replacer.get_right().get_height(), criminal_replacer.get_left().get_height()) + 1)
        # fix sizes
        criminal_original_size = criminal.get_size()
        criminal.set_size(criminal.get_size() - 1 - criminal_replacer.get_left().get_size())
        criminal_replacer.set_size(criminal_original_size)

    """left right rotation- same as in presentation"""

    def left_right_rotation(self, criminal):
        parent = criminal.get_parent()
        criminal_replacer = criminal.get_left().get_right()
        # update the criminal's parent child pointer
        if parent is not None:
            parent.set_child(criminal, criminal_replacer)
        else:
            self.root = criminal_replacer
        criminal_replacer.set_parent(parent)

        new_left = criminal.get_left()
        new_right = criminal

        # store new sizes for later
        criminal_new_size = criminal.get_right().get_size() + criminal_replacer.get_right().get_size() + 1
        new_left_new_size = (new_left.get_size() - 1 - criminal_replacer.get_right().get_size())
        criminal_replacer_new_size = criminal.get_size()

        criminal_replacer.get_left().set_parent(criminal.get_left())
        criminal.get_left().set_right(criminal_replacer.get_left())

        criminal_replacer.get_right().set_parent(criminal)
        criminal.set_left(criminal_replacer.get_right())

        criminal_replacer.set_left(new_left)
        new_left.set_parent(criminal_replacer)

        criminal_replacer.set_right(new_right)
        new_right.set_parent(criminal_replacer)
        # Fix heights
        criminal.set_height(max(criminal.get_right().get_height(), criminal.get_left().get_height()) + 1)
        new_left.set_height(max(new_left.get_right().get_height(), new_left.get_left().get_height()) + 1)
        criminal_replacer.set_height(
            max(criminal_replacer.get_right().get_height(), criminal_replacer.get_left().get_height()) + 1)

        # Fix sizes
        criminal.set_size(criminal_new_size)
        if new_left is not None:
            new_left.set_size(new_left_new_size)
        criminal_replacer.set_size(criminal_replacer_new_size)

    """right left rotation- same as in presentation"""

    def right_left_rotation(self, criminal):
        parent = criminal.get_parent()
        criminal_replacer = criminal.get_right().get_left()
        # update the criminal's parent child pointer
        if parent is not None:
            parent.set_child(criminal, criminal_replacer)
        else:
            self.root = criminal_replacer
        criminal_replacer.set_parent(parent)

        new_right = criminal.get_right()
        new_left = criminal

        # store new sizes for later
        criminal_new_size = criminal.get_left().get_size() + criminal_replacer.get_left().get_size() + 1
        new_right_new_size = (new_right.get_size() - 1 - criminal_replacer.get_left().get_size())
        criminal_replacer_new_size = criminal.get_size()

        criminal_replacer.get_right().set_parent(criminal.get_right())
        criminal.get_right().set_left(criminal_replacer.get_right())

        criminal_replacer.get_left().set_parent(criminal)
        criminal.set_right(criminal_replacer.get_left())

        criminal_replacer.set_right(new_right)
        new_right.set_parent(criminal_replacer)

        criminal_replacer.set_left(new_left)
        new_left.set_parent(criminal_replacer)
        # Fix heights
        criminal.set_height(max(criminal.get_right().get_height(), criminal.get_left().get_height()) + 1)
        new_right.set_height(max(new_right.get_right().get_height(), new_right.get_left().get_height()) + 1)
        criminal_replacer.set_height(
            max(criminal_replacer.get_right().get_height(), criminal_replacer.get_left().get_height()) + 1)

        # Fix sizes
        criminal.set_size(criminal_new_size)
        if new_right is not None:
            new_right.set_size(new_right_new_size)
        criminal_replacer.set_size(criminal_replacer_new_size)

    """inserts recursively a new node to the self tree with the given key and value.
    The method also updates the size field
    run time complexity- O(logn)
    """

    def bst_insert_rec(self, node, key, val):
        if key == node.get_key():
            node.value = val
            return node
        else:
            if key > node.get_key():
                if node.get_right().is_leaf():
                    res = AVLNode(key=key, value=val, parent=node)
                    node.set_right(res)
                else:
                    res = self.bst_insert_rec(node.get_right(), key, val)
            else:
                if node.get_left().is_leaf():
                    res = AVLNode(key=key, value=val, parent=node)
                    node.set_left(res)
                else:
                    res = self.bst_insert_rec(node.get_left(), key, val)
        node.size += 1
        return res

    """
    A recursive method that goes up in the tree, and updates the parents heights until there is no change in one height
    returns the number of updated heights
    run time complexity- O(logn)
    """

    def update_parents_height_after_insert(self, parent, updated_child_node, parents_updated=0):
        # If we reached the root
        if parent is None or updated_child_node is None:
            return parents_updated

        other_child = parent.get_right()
        if updated_child_node.get_is_right():
            other_child = parent.get_left()

        if other_child is None:
            return parents_updated
        # If the updated branch is the dominant one, add +1 to the height
        if not other_child.is_real_node() or updated_child_node.get_height() > other_child.get_height():
            parent.set_height(parent.get_height() + 1)
            parents_updated += 1
            if self.root != parent:
                return self.update_parents_height_after_insert(parent=parent.get_parent(), updated_child_node=parent,
                                                               parents_updated=parents_updated)
            else:
                return parents_updated
        else:
            return parents_updated

    """
    goes up in the tree, and updates the parents heights until there is no change in one height
    returns the number of updated heights
    run time complexity- O(logn)
    """

    def update_parents_height_after_deletion(self, parent, updated_child_node_height, other_child, parents_updated=0):
        if parent is None:
            return parents_updated

        if other_child is None:
            return parents_updated
        # If the updated branch is the dominant one, subtract 1 from the height
        if not other_child.is_real_node() or updated_child_node_height > other_child.get_height():
            original_parent_height = parent.get_height()
            parent.set_height(parent.get_height() - 1)
            parents_updated += 1
            if self.root != parent:
                return self.update_parents_height_after_deletion(parent=parent.get_parent(),
                                                                 other_child=parent.get_sibling(),
                                                                 updated_child_node_height=original_parent_height,
                                                                 parents_updated=parents_updated)
            else:
                return parents_updated
        else:
            return parents_updated

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    run time complexity- O(logn)
    same as the pseudo code we saw in class. 
    """

    def delete(self, node):
        if self.root is None or node is None:
            return 0  # shows there was nothing to delete
        physically_deleted_height, physically_deleted_sibling, physically_deleted_parent, node_to_fix_from = self.delete_from_bst(
            node)
        self.update_parents_height_after_deletion(
             updated_child_node_height=physically_deleted_height,
             other_child=physically_deleted_sibling,
             parent=physically_deleted_parent)
        return self.manage_rotation_after_deletion(physically_deleted_parent)

    """deletes the given node from the bst as we saw in class.
        run time complexity- O(logn)
    """

    def delete_from_bst(self, node):
        """ delete node"""
        node_to_delete_parent = node.get_parent()
        # 0 children
        if node.get_size() == 1:  # simply remove it
            res = node.get_height(), node.get_sibling(), node.get_parent(), node.get_parent()
            if self.root is node:  # there's only the root in this tree
                self.root = AVLNode(None, None, None)
            else:
                # update the parent's child to a virtual node so it wont be a part of the tree
                vir = AVLNode(None, None, None)  # virtual node
                vir.set_parent(node_to_delete_parent)
                node_to_delete_parent.set_child(node, vir)

        # 2 children
        elif is_real_node(node.get_right()) and is_real_node(node.get_left()):
            suc = self.successor(node)  # the successor
            if suc is node.get_right():
                node_to_delete_parent = suc
                res = suc.get_height(), suc.get_sibling(), suc, suc
            else:
                node_to_delete_parent = suc.get_parent()  # save it for later to update the sizes
                res = suc.get_height(), suc.get_sibling(), suc.get_parent(), suc
            # suc has no left child
            # remove suc from the tree
            suc.get_parent().set_child(suc, suc.get_right())
            suc.get_right().set_parent(suc.get_parent())
            suc.get_left().set_parent(suc.get_parent())
            # replace node by suc
            node.replace_with(suc)
            if self.root is node:
                self.root = suc

        # 1 child
        else:
            res = node.get_height(), node.get_sibling(), node.get_parent(), node.get_parent()
            if is_real_node(node.get_right()):  # only right child
                if node_to_delete_parent is not None:
                    node_to_delete_parent.set_child(node, node.get_right())
                else:  # if the parent is the root we need to update the root
                    self.root = node.get_right()
                node.get_right().set_parent(node_to_delete_parent)
            if is_real_node(node.get_left()):
                if node_to_delete_parent is not None:
                    node_to_delete_parent.set_child(node, node.get_left())
                else:  # if the parent is the root we need to update the root
                    self.root = node.get_left()
                node.get_left().set_parent(node_to_delete_parent)

        # update sizes of parents
        parent = node_to_delete_parent
        while is_real_node(parent):
            parent.size -= 1
            parent = parent.get_parent()
        return res

    """ manage the rotations after deletion of a node. 
    run time complexity- O(logn)- worst case going in a path from node to the root, as long as the height of the tree
    """

    def manage_rotation_after_deletion(self, parent):  # differnce is that more than one rotation is possible
        count_actions = 0
        # similar to manage_rotation_after_insertion excepts there can be a few rotations here
        while parent is not None:
            # update heights after rotation
            new_height = 1 + max(parent.get_right().get_height(),
                                 parent.get_left().get_height())
            if new_height != parent.get_height():
                count_actions += 1
                parent.set_height(new_height)
            balance = parent.get_balance()
            if abs(balance) == 2:
                count_actions += self.rotate_after_action(criminal=parent)
            parent = parent.get_parent()
        return count_actions

    """Finding the Next Item in a Running Order of Keys
     run time complexity- O(logn)
    """

    def successor(self, x):
        if x.get_right() is not None:
            return self.min_node(x.get_right())
        y = x.get_parent()
        while y is not None and x is y.get_right():
            x = y
            y = x.get_parent()
        return y

    """Finding the min node of the subtree that starts at the given node
       run time complexity- O(logn) worst case.
      """

    def min_node(self, x):
        while x.get_left() is not None and x.get_left().is_real_node():
            x = x.get_left()
        return x

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
     run time complexity- O(n).
    """

    def avl_to_array(self):
        if self.root is None:
            return []
        """
            inorder as we saw in class 
             run time complexity- O(n).
        """

        def in_order(node, res):
            if not is_real_node(node):
                return res
            in_order(node.get_left(), res)
            res.append((node.get_key(), node.get_value()))
            in_order(node.get_right(), res)

        res = []
        in_order(self.root, res)
        return res

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        if self.root is None:
            return 0
        return self.get_root().get_size()

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
     run time complexity- O(logn).
    """

    def split(self, node):
        # if we are splitting a tree of one node
        if self.size == 1:
            return [AVLTree(), AVLTree()]

        if self.root is node:
            self.root.get_right().set_parent(None)
            self.root.get_left().set_parent(None)
            return [tree_from_node(self.root.get_left()), tree_from_node(self.root.get_right())]

        smaller_members = []  # t1 in the presentation
        bigger_members = []  # t2 in the presentation

        # create subtrees from the children of the node to split on
        left_sub_tree = tree_from_node(node.get_left())  # D in the presentation
        right_sub_tree = tree_from_node(node.get_right())  # H in the presentation

        parent = node.get_parent()
        while parent is not None:
            # Fill the arrays with the trees and the nodes as tuples
            if node is parent.get_right():
                smaller_members.append((parent, tree_from_node(parent.get_left())))
            else:
                bigger_members.append((parent, tree_from_node(parent.get_right())))
            node = parent
            parent = parent.get_parent()
        t1 = left_sub_tree
        for node, tree in smaller_members:
            t1.join(tree, node.get_key(), node.get_value())

        t2 = right_sub_tree
        for node, tree in bigger_members:
            t2.join(tree, node.get_key(), node.get_value())

        return [t1, t2]

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
     run time complexity- O(logn).
    """

    def join(self, tree, key, val):
        if not is_real_node(self.root):  # tree will be the whole tree
            tree_h = tree.root.get_height()  # other tree height
            self.root = tree.root
            self.insert(key, val)  # add the given node that's in the middle
            return tree_h + 1

        if not is_real_node(tree.root):
            self_h = self.root.get_height()  # self height
            self.insert(key, val)
            return self_h + 1

        self_h = self.root.get_height()  # self height
        tree_h = tree.root.get_height()  # other tree height
        diff = abs(self_h - tree_h)

        x = AVLNode(key, val, None)

        # check which tree has the bigger keys:
        # use as in presentation- T1 < x < T2
        if self.root.get_key() > key:
            T2 = self
            T1 = tree

        else:  # other.root.key > key, then it has the bigger keys
            T2 = tree
            T1 = self

        # if both trees are in the same height,
        # or the diff in the heights <1 then the tree will stay balanced after joining
        if self_h == tree_h or diff == 1:
            # attach to x as the left child the tree with the smaller keys
            x.set_left(T1.root)
            T1.root.set_parent(x)
            x.set_right(T2.root)
            T2.root.set_parent(x)
            x.set_size(T1.root.get_size() + T2.root.get_size() + 1)
            self.root = x  # now it will be as in presentation    x
            #                                     /  \
            #                                    T1    T2
            x.set_height(max(self_h, tree_h) + 1)
            return diff + 1
        # check which tree is the highest one:
        if T1.root.get_height() < T2.root.get_height():  # T2 is the highest one
            # act as the case in the presentation
            a = T1.root
            h = a.get_height()
            b = T2.root
            # we should find b – first vertex on the left spine of T2 with height ≤ h
            while b.get_height() > h:
                b = b.get_left()

            # now b's height should be <= h
            c = b.get_parent()
            c.set_left(x)
            b.set_parent(x)
            x.set_parent(c)
            x.set_right(b)
            x.set_left(a)
            a.set_parent(x)
            x.set_size(a.get_size() + b.get_size() + 1)
            x.set_height(h + 1)
            self.root = T2.root
            parent = c
            while parent is not None:
                parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                parent = parent.get_parent()

            #            c---
            #           /
            #          x
            #         /  \
            #        a     b
            #        T1    /\

            #  now need to do rebalancing from x upwards, if needed

            heights_updated_count = self.update_parents_height_after_insert(parent=x.get_parent(),
                                                                            updated_child_node=x)
            self.manage_rotation_after_deletion(x)
            return diff + 1
        else:  # T1 is the highest one (and the one with the snaller keys)
            # act opposite to the case in the presentation
            a = T1.root
            b = T2.root
            h = b.get_height()
            # we should find a – first vertex on the right spine of T1 with height ≤ h
            while a.get_height() > h:
                a = a.get_right()
            # now a's height should be <= h
            c = a.get_parent()
            c.set_right(x)
            b.set_parent(x)
            x.set_parent(c)
            x.set_right(b)
            x.set_left(a)
            a.set_parent(x)
            x.set_size(a.get_size() + b.get_size() + 1)
            x.set_height(h + 1)
            self.root = T1.root
            parent = c
            while parent is not None:
                parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
                parent = parent.get_parent()

            #        c---
            #         \
            #          x
            #         /  \
            #        a     b
            #        T1    /\

            #  now need to do rebalancing from x upwards, if needed

            self.update_parents_height_after_insert(parent=x.get_parent(), updated_child_node=x)

            self.manage_rotation_after_deletion(x) #acting as in deletion
            # finally, return the cost - the diff of the tree's heights  + 1
            return diff + 1

    """compute the rank of node in the self

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    run time complexity- O(logn).
    """

    # Rank = position in sorted order
    def rank(self, node):
        # Works exactly like the rank in the presentation
        rank = 1 + node.get_left().get_size()
        child = node
        parent = node.get_parent()
        while parent is not None:
            if child is parent.get_right():
                rank += parent.get_left().get_size() + 1
            child = parent
            parent = parent.get_parent()
        return rank

    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    run time complexity- O(logn).
    """

    def select(self, i):
        def select_rec(x, k):
            if not is_real_node(x):
                return None  # item of rank k isn't exist
            r = x.get_left().get_size() + 1
            if k == r:
                return x  # the root is the required element
            elif k < r:
                return select_rec(x.get_left(), k)  # search for the k'th smallest item in the left subtree of the root
            else:  # k > r
                return select_rec(x.get_right(),
                                  k - r)  # search for the (k-r)th smallest item in the right subtree of the root

        return select_rec(self.root, i)

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root
