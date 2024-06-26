# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

from PrintTreeUtil import *

"""A class represnting a node in an AVL tree"""


def is_real_node(node):
    return node is not None and node.is_real_node()


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

    def __repr__(self):  # no need to understand the implementation of this one
        return f"key={self.key} value={self.value}"

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

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
        if h < -1:
            print('setting negative height')
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

    #
    # def get_depth(self):
    #     return self.depth
    #
    # def set_depth(self, d):
    #     self.depth = d

    def is_real_node(self):
        return self.key is not None

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

    def set_child(self, old_child, new_child):
        if old_child is self.right:
            self.set_right(new_child)
        elif old_child is self.left:
            self.set_left(new_child)

    def get_children_count(self):
        res = 0
        if is_real_node(self.get_right()):
            res += 1
        if is_real_node(self.get_left()):
            res += 1
        return res

    # if self.left.is_leaf() and self.right.is_leaf()

    # child_to_insert = self.left
    # if key > self.key:
    #     child_to_insert = self.right
    # if child_to_insert.is_leaf():
    #     child_to_insert = AVLNode(key=key, value=val, parent=self)
    # else:
    #     child_to_insert.insert(key, val)
    def replace_with(self, other):
        if self.get_parent() is not None:
            self.get_parent().set_child(self, other)
        other.set_parent(self.get_parent())

        if is_real_node(self.get_right()):
            self.get_right().set_parent(other)
        other.set_child(other.get_right(), self.get_right())

        if is_real_node(self.get_left()):
            self.get_left().set_parent(other)
        other.set_child(other.get_left(), self.get_left())

        other.set_size(self.get_size())
        other.set_height(self.get_height())

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
        self.max_node = None
        self.visited=0

    # add your fields here

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        if self.root is None:
            return None
        node = self.root
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
    """

    def insert(self, key, val):
        # BST insertion
        if not is_real_node(self.root):
            self.root = AVLNode(key=key, value=val, parent=None)
        else:
            inserted = self.bst_insert_rec(node=self.root, key=key, val=val)
            heights_updated_count = self.update_parents_height_after_insert(parent=inserted.get_parent(),
                                                                            updated_child_node=inserted)
            return heights_updated_count + self.manage_rotation_after_insert(inserted, heights_updated_count)

    def manage_rotation_after_insert(self, inserted, height_updated_count):
        loop_counter = height_updated_count
        parent = inserted.get_parent()
        # algorithm exactly as pseudo code in presentation - can be refactoed with for loop probably
        while parent is not None:
            loop_counter -= 1
            balance = parent.get_balance()
            if abs(balance) < 2 and loop_counter == 0:
                return 0
            elif abs(balance) < 2 and loop_counter > 0:
                parent = parent.get_parent()
            else:  # balance ==2
                criminal_before_rotation = parent
                criminal_parent_before_rotation = parent.get_parent()
                self.rotate_after_action(criminal=parent)
                height_to_update = criminal_parent_before_rotation
                # fix all heights starting from original criminal's parent
                # for i in range(height_updated_count - 2):
                for i in range(height_updated_count - criminal_before_rotation.get_height() - 2):
                    if height_to_update is None:
                        break
                    height_to_update.set_height(height_to_update.get_height() - 1)
                    height_to_update = height_to_update.get_parent()
                return 1
        return 0

    def rotate_after_action(self, criminal):  # rotate after insertion or deletion
        if criminal.get_balance() == -2:
            right_child_balance = criminal.get_right().get_balance()
            if right_child_balance == -1 or right_child_balance == 0:  # notice that after insertion the bf of son can't be 0, only after deletion
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
            elif left_child_balance == 1 or left_child_balance == 0:
                self.right_rotation(criminal)
                return 1
        return 0

    def left_rotation(self, criminal):
        # print("left rotation")
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

    def right_rotation(self, criminal):
        # print("right rotation")
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

    def left_right_rotation(self, criminal):
        # print("left right rotation")
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

    def right_left_rotation(self, criminal):
        # print("right left rotation")
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


    def bst_insert_rec2(self, node, key, val):
        self.visited+=1
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
    goes up in the tree, and updates the parents heights until there is no change in one height
    returns the number of updated heights
    """

    def update_parents_height_after_insert(self, parent, updated_child_node, parents_updated=0):
        if parent is None or updated_child_node is None:
            return parents_updated

        other_child = parent.get_right()
        if updated_child_node.get_is_right():
            other_child = parent.get_left()

        if other_child is None:
            return parents_updated

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

    def update_parents_height_after_deletion(self, parent, updated_child_node, other_child, parents_updated=0):
        if parent is None or updated_child_node is None:
            return parents_updated

        if other_child is None:
            return parents_updated

        if not other_child.is_real_node() or updated_child_node.get_height() > other_child.get_height():
            parent.set_height(parent.get_height() - 1)
            parents_updated += 1
            if self.root != parent:
                return self.update_parents_height_after_deletion(parent=parent.get_parent(), other_child=other_child,
                                                                 updated_child_node=parent,
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
    """

    def delete(self, node):
        if self.root is None or node is None:
            return -1  # shows there was nothing to delete
        physically_deleted, physically_deleted_sibling, physically_deleted_parent, node_to_fix_from = self.delete_from_bst(
            node)
        heights_updated_count = self.update_parents_height_after_deletion(updated_child_node=physically_deleted,
                                                                          other_child=physically_deleted_sibling,
                                                                          parent=physically_deleted_parent)
        return heights_updated_count + self.manage_rotation_after_deletion(node_to_fix_from,
                                                                           heights_updated_count)

    # differences between Insertion and Deletion
    ## returns physically_deleted, physically_deleted_sibling, physically_deleted_parent, node_to_fix_from
    def delete_from_bst(self, node):
        """ delete node"""
        node_to_delete_parent = node.get_parent()
        # 0 children
        if node.get_size() == 1:  # simply remove it
            res = node, node.get_sibling(), node.get_parent(), node.get_parent()
            if self.root is node:  # there's only the root in this tree
                self.root = AVLNode(None, None, None)
            else:
                # update the parent's child to a virtual node so it wont be a part of the tree
                node_to_delete_parent.set_child(node, AVLNode(None, None, None))

        # 2 children
        elif is_real_node(node.get_right()) and is_real_node(node.get_left()):
            y = self.successor(node)
            res = y, y.get_sibling(), y.get_parent(), y
            # height_of_y_after_replace=max(node.get_right().get_height(),node.get_left().get_height())+1
            # y has no left child
            # remove y from the tree
            y.get_parent().set_child(y, y.get_right())
            if is_real_node(y.get_right()):
                y.get_right().set_parent(y.get_parent())
            # replace node by y
            node.replace_with(y)
            y.set_size(y.get_size() - 1)
            if self.root is node:
                self.root = y

        # 1 child
        else:
            res = node, node.get_sibling(), node.get_parent(), node.get_parent()
            if is_real_node(node.get_right()):  # only right child
                node_to_delete_parent.set_child(node, node.get_right())
            if is_real_node(node.get_left()):
                node_to_delete_parent.set_child(node, node.get_left())

        # update sizes of parents
        parent = node_to_delete_parent
        while is_real_node(parent):
            parent.size -= 1
            parent = parent.get_parent()
        return res

    def manage_rotation_after_deletion(self, parent,
                                       height_updated_count):  # differnce is that more than one rotation is possible
        loop_counter = height_updated_count
        count_actions = 0
        # algorithm exactly as pseudo code in presentation - can be refactoed with for loop probably
        while parent is not None:
            loop_counter -= 1
            balance = parent.get_balance()
            if abs(balance) < 2 and loop_counter == 0:
                return count_actions
            elif abs(balance) < 2 and loop_counter > 0:
                parent = parent.get_parent()
                continue
            else:  # balance ==2
                criminal_parent_before_rotation = parent.get_parent()
                count_actions += self.rotate_after_action(criminal=parent)
                height_to_update = criminal_parent_before_rotation
                # fix all heights starting from original criminal's parent
                for i in range(height_updated_count - 2):
                    if height_to_update is None:
                        break
                    height_to_update.set_height(height_to_update.get_height() - 1)
                    count_actions += 1
                    height_to_update = height_to_update.get_parent()
                parent = parent.get_parent()
        return count_actions

    # Finding the Next Item in a Running Order of Keys
    def successor(self, x):
        if x.get_right() is not None:
            return self.min_node(x.get_right())
        y = x.get_parent()
        while y is not None and x is y.get_right():
            x = y
            y = x.get_parent()
        return y

    # maybe better to add pointer to the min node?
    def min_node(self, x):
        while x.get_left() is not None and x.get_left().is_real_node():
            x = x.get_left()
        return x

    """returns an array representing dictionary 
    
    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        if self.root is None:
            return []

        def in_order(node, res):
            if node is None:
                return res
            if is_real_node(node.get_left()):
                in_order(node.get_left(), res)
            res.append((node.get_key(), node.get_value()))
            if is_real_node(node.get_right()):
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
    """

    def split(self, node):
        work = 0
        max_join_work = 0
        if self.size == 1:
            return [AVLTree(), AVLTree()]
        x = node
        t1_members = []
        t2_members = []

        D = tree_from_node(x.get_left())
        H = tree_from_node(x.get_right())

        parent = node.get_parent()
        while parent is not None:
            if node is parent.get_right():
                t1_members.append((parent, tree_from_node(parent.get_left())))
            else:
                t2_members.append((parent, tree_from_node(parent.get_right())))
            node = parent
            parent = parent.get_parent()

        t1 = D
        for node, tree in t1_members:
            current_work = t1.join(tree, node.get_key(), node.get_value())
            work += current_work
            if current_work > max_join_work:
                max_join_work = current_work
        t2 = H
        for node, tree in t2_members:
            current_work = t2.join(tree, node.get_key(), node.get_value())
            work += current_work
            if current_work > max_join_work:
                max_join_work = current_work

        joins_count = len(t1_members) + len(t2_members)
        if joins_count == 0:
            average = 0
        else:
            average = work / joins_count
        print(f'average join work: {average}, max join work: {max_join_work}')

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

        # if both trees are in the same height, or the diff in the heights <1 then the tree will stay balanced after joining
        if self_h == tree_h or diff == 1:
            # attach to x as the left child the tree with the smaller keys
            x.set_left(T1.root)
            T1.root.set_parent(x)
            x.set_right(T2.root)
            T2.root.set_parent(x)
            self.root = x  # now it will be as in presentation    x
            #                                     /  \
            #                                    T1    T2
            x.set_height(max(self_h, tree_h) + 1)
            x.set_size(T1.root.get_size() + T2.root.get_size() + 1)
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
                if b is None:
                    print('stop')
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
                # parent.set_height(max(parent.get_left().get_height() + 1, parent.get_right().get_height()) + 1)
                parent = parent.get_parent()

            #            c---
            #           /
            #          x
            #         /  \
            #        a     b
            #        T1    /\

            #  now need to do rebalancing from x upwards, if needed

            # todo: rebalancing here!
            heights_updated_count = self.update_parents_height_after_insert(parent=x.get_parent(),
                                                                            updated_child_node=x)
            self.manage_rotation_after_deletion(x, heights_updated_count)
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
                # parent.set_height(max(parent.get_left().get_height() +1, parent.get_right().get_height() +1))
                parent = parent.get_parent()

            #        c---
            #         \
            #          x
            #         /  \
            #        a     b
            #        T1    /\

            #  now need to do rebalancing from x upwards, if needed
            # todo: rebalancing here!
            # print("before balance")
            # print(self)

            heights_updated_count = self.update_parents_height_after_insert(parent=x.get_parent(),
                                                                            updated_child_node=x)
            # print("after update parents")
            self.manage_rotation_after_deletion(x, heights_updated_count)
            # finally, return the cost - the diff of the tree's heights  + 1
            # print("after balance")
            return diff + 1

    """compute the rank of node in the self
    
    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    # Rank = position in sorted order
    def rank(self, node):
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

    def find_sub_tree_root_for_insert_from_max(self, key, node_to_search_from, node_searched_count):
        current = node_to_search_from
        if current is self.root:
            return self.root, node_searched_count + 1
        parent = current.get_parent()
        if key > current.get_key():
            return current, node_searched_count + 1
        if key < current.get_key() and key > parent.get_key():
            return parent, node_searched_count + 1
        if key < current.get_key() and key < parent.get_key():
            return self.find_sub_tree_root_for_insert_from_max(key, parent, node_searched_count + 1)
        # print('error in conditions - maybe we have duplicate keys')

    def bst_insert_from_max(self, key, value):
        sub_tree_root, nodes_searched_count = self.find_sub_tree_root_for_insert_from_max(key, self.max_node, 0)
        inserted = self.bst_insert_rec2(sub_tree_root, key, value)
        if self.max_node is None or key > self.max_node.get_key():
            self.max_node = inserted
        heights_updated_count = self.update_parents_height_after_insert(parent=inserted.get_parent(),
                                                                        updated_child_node=inserted)
        return inserted,heights_updated_count + self.manage_rotation_after_insert(inserted,
                                                                         heights_updated_count) + nodes_searched_count + self.visited

    def validate_heights(self):
        self.validate_heights_rec(self.root)

    def validate_heights_rec(self, node):
        if is_real_node(node):
            if node.is_leaf():
                if node.height != 0:
                    print(f'error in leaf height key={node.key}')
            else:
                if node.height != 1 + max(node.get_right().height, node.get_left().height):
                    print(f'error in node height key={node.key}')

    def __repr__(self):  # no need to understand the implementation of this one
        # return "tree"
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out
