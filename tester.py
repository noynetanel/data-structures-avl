import random

from AVLTree import AVLTree

# n=11
# keys = [k for k in range(n)]
keys=[1,5,10,15,20,25,30,35,40]
tree1 = AVLTree()
for key in keys:
    tree1.insert(key, key)

print(tree1)
# random.shuffle(keys)
# keys=keys[1]
# for key in range(n-1):
#     print(f'deleting {key}')
#     node=tree1.search(key)
#     tree1.delete(node)
#     print(tree1)
#     tree1.validate_heights()
#



# random_key = 399
# random_node = tree1.search(random_key)
# tree1.split(random_node)


#keys=[10,5,20,3,8,18,25,2,4,6,9,15,22,16]
# keys=[100,20,50,10,15,7]
# keys.reverse()
# t1 = AVLTree()
# for i in keys:
#     t1.insert(i, 0)
#     print(t1)
#
# num = t1.search(50)
# print('deleting')
# print(t1.delete_from_bst(num))
# print(t1)

# keys = [15,8,22,24,4,11,20,18,12,9,2,13]
# t1 = AVLTree()
# for i in keys:
#     t1.insert(i, 0)
# print(t1)
# node= t1.search(22)
# print(t1.delete(node))
# print(t1)

# arr = t1.avl_to_array()
# print(arr)
# t2 = AVLTree()
# print(t2.avl_to_array())
#
# keys = [4, 5, 7]
# t1 = AVLTree()
# for i in keys:
#     t1.insert(i, 0)
#
# print('t1 before join')
# print(t1)
#
# t2 = AVLTree()
# keys = [20,19,22,30,50,70,15]
# for i in keys:
#     t2.insert(i, 0)
# print('t2 before join')
# print(t2)
# print('joining')
# print(t1.join(t2, 10,0))
# print(t1)
#
# print('spliting')
# x=t1.search(5)
# res=t1.split(x)
# print('t1')
# print(res[0])
# print('t2')
# print(res[1])
#



# num = t1.search(7)
# print('deleting')
# print(t1.delete_from_bst(num))
# print(t1)
#
# num = t1.search(10)
# print('deleting')
# print(t1.delete_from_bst(num))
# print(t1)

# keys2 = [8,10,5,4,6]
# t2 = AVLTree()
# for key in keys2:
#     t2.insert(key, 0)
# print(t2)
# ten = t2.search(10)
# print(t2.delete(ten))
# print(t2)

# t1.insert(5, 0)
# print(t1)

# print(t1.get_root().get_right())
# print(t1.get_root().get_left())
# print(t1)
# t1.insert(2,0)
# print(t1)
# t1.insert(1,0)
# print(t1)
# t1.insert(3,0)
# print(t1)
# t1.insert(4,0)
# print(t1)
# t1.insert(-10,0)
# print(t1)
# t1.insert(5,0)
# print(t1)
# t1.insert(2.5,0)
# print(t1)
# t1.insert(60,0)
# print(t1)

[]
