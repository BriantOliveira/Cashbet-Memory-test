
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


