# You're welcome to use this decorator
# See: https://www.geeksforgeeks.org/python/python-functools-total_ordering/
from functools import total_ordering
import math

from typing import Union
from data_structures import ArrayList, ArrayR
from data_structures.binary_search_tree import BinarySearchTree, K, V
from data_structures import Node

class BetterBinarySearchTree(BinarySearchTree[K, V]):
    def __init__(self) -> None:
        super().__init__()
        
    def range_query(self, low: K, high: K) -> Union[ArrayR[V], ArrayList[V]]:
        """
            Return all items from the BST with keys,
            in the (inclusive) range of [low, high].
            Return the result in either an ArrayR or an ArrayList.
            Complexity Analysis
            Best Case: O(h+k) where h is the height of the tree and k the number of retured items. 
            h: For a balance tree it's O(logn) which is the best case. 
            Worst Case: O(h+k) where h is the height of the tree and k the number of retured items. 
            h: For a unbalnce tree it's O(n) which is the worst case. 
            ...
        """
        result = ArrayList[V]()
        self.binary_tree_traversal(self.__root, low, high, result)
        return result 
    
    def binary_tree_traversal(self,current:BinarySearchTree[K,V], low:K,high:K, result: ArrayList[V]) -> None: 
        if current is None: 
            return 
        if current.key > low:
            self.binary_tree_traversal(current.left,low,high,result)
        if low <= current.key <= high:
            result.append(current.item)
        if current.key < high :
            self.binary_tree_traversal(current.right,low,high,result)
            

    def balance_score(self):
        """
            Returns the balance score of the BST, which we define as the
            difference between the ideal (balanced) height of the tree (achievable with a complete tree),
            and the actual height of the tree.
            Complexity Analysis: 
            Best: O(n)
            Worst: O(n) Overall complexity is same because to calculate the height it should 
            vist every node. n is the number of nodes 
            ...
        """
        def height_calculate(node) -> int:
            if node is None : 
                return 0
            else: 
                left_h = height_calculate(node.left)
                right_h = height_calculate(node.right)
                return 1 + max(left_h,right_h)
        actual_height = height_calculate(self.__root)
        n = len(self)
        
        if n == 0 :
            balance_height = 0 
        else : 
            balance_height = math.floor(math.log2(n))
        return actual_height - balance_height
       
        
    
    def rebalance(self):
        """
            Restructure the BST such that it is balanced.
            Do *not* return a new instance; rather, this method
            should modify the tree it is called on.
            Complexity Analysis:
            The items() function goes through every node once to collect to collect them, so this is O(n)
            Then the build_balnce_tree function also goes through every node to build the tree back 
            The Complexity winds upto: O(n) + O(n)
            Thefore the overall complexity is O(n)
            ...
        """
        items = self.items()
        
        def build_balnce_tree(start,end):
            if start > end: 
                return None
            else : 
                mid = (start+end)//2 
                key,value = items[mid]
                node = self.__root.__class__(value,key,0)
                node.left = build_balnce_tree(start,mid-1)
                node.right = build_balnce_tree(mid+1,end)
                return node
        self.__root = build_balnce_tree(0,len(items)-1)

if __name__ == "__main__":
    # Test your code here.
    
    # Create a Better BST
    bbst = BetterBinarySearchTree()
    
    # Add all integers as key-value pairs to the tree
    for i in range(10):
        bbst[i] = i
        
    # Try a range query
    # Should give us the values between 4 and 7
    print("Range query:", bbst.range_query(4, 7))
    
    # Check the balance score before balancing
    print("Before balancing:", bbst.balance_score())
    
    # Try a rebalance
    bbst.rebalance()
    
    # How about after?
    print("After balancing:", bbst.balance_score())
