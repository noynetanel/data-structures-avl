from AVLTree import *
import random

# Q1


# def swaps_number(arr1):
#     size=len(arr1)
#     for i in range(size):
#         for j in range(i+1,len(range()))
#


for i in range(1, 6):
    total_work = 0
    swaps_count = 0
    n = 1500 * (2 ** i)
    tree = AVLTree()
    print(f'n={n}')
    print(n * (n - 1) // 2)
    tree.insert(n, n)
    tree.max_node = tree.search(n)
    keys = [k for k in range(n - 1, 0, -1)]
    keys = [n] + keys
    for i in range(len(keys)):
        inserted, worked = tree.bst_insert_from_max(keys[i], keys[i])
        total_work += worked
        inserted_rank = tree.rank(inserted)
        if (inserted_rank != 1):
            print('error in rank')
        if i > 0:
            swaps_count += i + 1 - inserted_rank
    print(f'total work={total_work}, swaps count={swaps_count}')

#
# keys=[1,5,10,15,20,25,30,35]
# tree = AVLTree()
# tree.insert(40, 40)
# tree.max_node = tree.search(40)
#
# for key in keys:
#     tree.bst_insert_from_max(key, key)
#
#
# for k in keys:
#     print(f'{k} rank is {tree.rank(tree.search(k))}')

# # Q2
#
#
# for i in range(1, 11):
#     print(f'i={i}')
#     n = 1500 * (2 ** i)
#     keys = [k for k in range(n)]
#     random.shuffle(keys)
#
#     tree1 = AVLTree()
#     for key in keys:
#         tree1.insert(key,key)
#     random_key=random.choice(keys)
#     random_node=tree1.search(random_key)
#     tree1.split(random_node)
#
#
