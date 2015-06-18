class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self.item)


class BinarySearchTree:
    def __init__(self,root=None,left=None,right=None):
        self.root = Node(root)
        self.root.left = left
        self.root.right = right

    def insert(self,val):
        if self.root.item == None:
            self.root = Node(val)
        else:
            self._insert(self.root,val)

    def _insert(self,curr,val):
        if curr.item > val and curr.left == None:
            node = Node(val)
            curr.left = node
        elif curr.item < val and curr.right == None:
            node = Node(val)
            curr.right = node
        else:
            if curr.item < val:
                self._insert(curr.right,val)
            else:
                self._insert(curr.left,val)

    def contains(self,val):
        if self.root.item == val:
            return True
        else:
            return self._contains(self.root,val)
    
    def _contains(self,curr,val):
        
        if curr.item == val:
            return True
        if val < curr.item:
            if curr.left != None:
                return self._contains(curr.left,val)
            else:
                return False
        elif val > curr.item:
            if curr.right != None: 
               return self._contains(curr.right,val)
            else:
                return False
        else:
            return False

    def pretty_print(self):
        if self.root.item == None:
            print None
        else:
            self._pretty_print(self.root,0)
    
    def _pretty_print(self,curr,count):
        if curr.item == None:
            print None
        else:
            if curr.left != None:
                self._pretty_print(curr.left,count+1)
            print (" "*count)+str(curr.item)
            if curr.right != None:
                self._pretty_print(curr.right,count+1)



    def second_highest_node(self,node):
        if node.right != None:
            return self._second_highest_node(node)
        else:
            return None

    def _second_highest_node(self,curr):
        next_node = curr.right
        if next_node.right != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def highest(self,node):
        return self._highest(node)
        
    def _highest(self,curr):
        if curr.right != None:
            return self._highest(curr.right)
        else:
            return curr.item
    
    def second_lowest_node(self,node):
        if node.left != None:
            return self._second_lowest_node(node)
        else:
            return None
    def _second_lowest_node(self,curr):
        next_node = curr.left
        if next_node.left != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def lowest(self,node):
        return self._lowest(node)

    def _lowest(self,curr):
        if curr.left != None:
            return self._lowest(curr.left)
        else:
            return curr.item

    def delete(self,value):
        return self._delete(self.root,value,None)

    def _delete(self,curr,value,parent):
        if value == curr.item:
            if curr.left != None:
                curr.item = self.highest(curr.left)
                second_largest_node = self.second_highest_node(curr.left)
                if second_largest_node != None:
                    second_largest_node.right = None
                    return value
                else:
                    curr.left = None
                    return value 

            elif curr.right != None:
                curr.item = self.lowest(curr.right)
                second_smallest_node = self.second_lowest_node(curr.right)
                if second_smallest_node != None:
                    second_smallest_node.left = None
                    return value
                else:
                    curr.right = None
                    return value
            else:
                if parent.left.item == value:
                    parent.left = None
                    return value
                else:
                    parent.right = None
                    return value
                
        else:
            if value < curr.item and curr.left != None:
                self._delete(curr.left,value,curr)
            elif value > curr.item and curr.right != None:
                self._delete(curr.right,value,curr)
            else:
                
                return None

