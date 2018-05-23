
class HeapTree(object):

    def __init__(self, items=None):
        """Initialize the heap and insert the giving item"""
        self.items = []
        if items:
            for item in items:
                self.insert(item)
    
    def __repr__(self):
        """Return a string representation of this heap"""
        return 'HeapTree({})'.format(self.items)

    def is_empty(self):
        """Return a bool if the heap is empty or not"""
        if self.items == []:
            return True
        return False

    def size(self):
        """Return the number of items in the tree"""
        return len(self.items)

    def insert(self, item):
        """Insert the item at the end on the bubble up"""
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """Return the minimum item at the root of the tree
        The worst running time will be O(1) because the min is the root.
        """
        if self.size() == 0:
            raise ValueError("Heap tree is empty")
        assert self.size() > 0
        return self.items[0]

    def delete_min(self):
        if self.size() == 0:
            raise ValueError("The Heap has no minimum value")
        elif self.size() == 1:
        min_item = self.items.pop()
        assert self.size[0]
        #Move the last item tot the root and bubble down tot he leaves
        last_item = self.items.pop()
        self.items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def replace_min(self, item):
        """Remove and return the minimum item at the root of this heap, and insert the given 
        item into the heap, and insert the given item into the heap
        """
        if self.size == 0:
            raise ValueError("The heap tree is empty and has no minimum value")
        assert self.size() > 0
        min_item = self.items[0]
        #Replace the root and bubble down to the leaves
        self.items[0] = item
        if self.size() > 1:
            self._bubble_down(0)
            return min_item

    def _bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index, 
        swapping out the order items, until the root node is reached.
        """
        if index == 0:
            return  #This is the root node. 
        if not (0 <= self._last_index()):
            raise IndexError("Invalid index: {}".format(index))
        # Get the item value
        item = self.items[index]
        # Get the parent's index and value
        parent_index = self._parent_index(index)
        parent_item = self.items[parent_index]

        # Swap this item with parent item if values are out of order
        did_swap = False
        if item < parent_item:
            self.items[parent_index] = item
            self.items[index] = parent_item
            did_swap = True

        # Recursively bubble up
         if did_swap is True:
             self._bubble_up(parent_index)

    def _bubble_down(self, index):
        if not (0 <= self._last_index()):
            raise ValueError("")
