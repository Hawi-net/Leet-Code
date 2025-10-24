class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.to_peek

    def next(self):
        """
        :rtype: int
        """
        temp = self.to_peek
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None
        return temp

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.to_peek is not None