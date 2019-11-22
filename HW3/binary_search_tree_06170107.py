# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#        :type val: int
#        :type left: TreeNode or None
#        :type right: TreeNode or None
       
class Solution(object):
    def __init__(self):
        self.sear = None
        self.node = None
        self.target = None
        self.count = 0
        self.tree = 0
        self.r=0
        self.l=0
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val == None:
            root(val)
        else:
            if val <= root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    self.node = root.left
                else:
                    self.insert(root.left, val)
            else:
                if root.right == None:
                    root.right = TreeNode(val)
                    self.node = root.right
                else:
                    self.insert(root.right, val)
            return self.node
    def change(self,root):
        if root.right == None and root.left == None:
            return None
        elif root.right != None and root.left != None:
            j = root.left
            while j.right != None:
                j = j.right
            root.val = j.val
            root.left = self.delete(root.left,root.val)
            return root
        elif root.right != None and root.left == None:
            j = root.right
            while j.left != None:
                j = j.left
            root.val = j.val
            root.right = self.delete(root.right,root.val)
            return root
        elif root.right == None and root.left != None:
            j = root.left
            while j.right != None:
                j = j.right
            root.val = j.val
            root.left = self.delete(root.left,root.val)
            return root
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """ 
        if self.target == None:
            self.target = target
        if target < root.val:
            if root.left == None:
                return
            else:
                root.left = self.delete(root.left, target)
                return root
        elif target > root.val:
            if root.right == None:
                return
            else:
                root.right = self.delete(root.right, target)
                return root
        elif root.val == target:
            root = self.change(root)
            if root != None and root.val == self.target:
                root = self.change(root)
            return root
        
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target < root.val:
            if root.left == None:
                self.sear = None
            else:
                self.search(root.left, target)
        elif target > root.val:
            if root.right == None:
                self.sear = None
            else:
                self.search(root.right, target)
        elif target == root.val:
            self.sear = root
        return self.sear
    
    def count_target(self, root, target):
        while root != None:
            if root.val == target:
                self.count+=1
                root = root.left
            elif root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
    def tree_high(self, root, high):
        if root.right != None:
            self.r = high + 1
            self.r = self.tree_high(root.right, self.r)
        if root.left != None:
            self.l = high + 1
            self.l = self.tree_high(root.left, self.l)
        if self.l >= self.r:
            return self.l
        elif self.l<self.r:
            return self.r
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        self.tree = self.tree_high(root, 1)
        if root.left == None and root.right == None:
            self.tree = 1
        self.count_target(root,target)
        if self.count == 0:
            return
        self.delete(root,target)
        self.node = self.insert(root, new_val)
        if self.tree_high(root, 1) + 1 <= self.tree:
            pass
        else:
            if root.val >= new_val:
                x = root
                root = x.left
                x.left = root.right
                root.right = x
            else:
                x = root
                root = x.right
                x.right = root.left
                root.left = x
        self.count = self.count - 1
        if self.count > 0:
            self.modify(root, target, new_val)
        return self.node
