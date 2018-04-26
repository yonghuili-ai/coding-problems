"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix, where the index of the list is equal to the integer 
stored in that node and a 1 represents a child node, r is a non-negative integer representing the root,
and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.


As the tree is binary search tree, we do it recursively. We check whether one of the two nodes are
equal to the root, if so, return the root value. 
Otherwise there are 3 situations:
1. the root value are between the two nodes' value, if so, the root is the common ancestor.
2. the two nodes' values are smaller than the root value, then firstly we find the root's left child
by looking at the matrix row r starting from the left, the first non-zero element is correspoding to
the left child. Then we run the same procedure on the root's left child.
3. the two nodes' values are larger than the root value, then firstly we find the root's right child
by looking at the matrix row r starting from the right, the first non-zero element is correspoding to
the right child. Then we run the same procedure on the root's right child.
The space complexity is O(1)
Suppose the matrix is N times N. The time complexity is O(N^2)

"""
def question4(T, r, n1, n2):
    if not T:
        return None
    if n1 == r or n2 == r:
        return r
    if (n1 < r and n2 > r) or (n1 > r and n2 < r):
        return r
    if n1 < r and n2 < r:
        for i in range(len(T[r])):
            if T[r][i] != 0:
                return question4(T, i, n1, n2)
    if n1 > r and n2 > r:
        for i in range(len(T[r])-1, -1, -1):
            if T[r][i] != 0:
                return question4(T, i, n1, n2)
    return None
print("question 4")
# test case 1, print out 3
print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))
# test case 2, print out 0
print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          0))
# test case 3, print out None
print(question4([],
          None,
          1,
          4))

