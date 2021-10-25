#!/usr/bin/python3
""" Create a class FIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but
don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None. """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_list(array):
        """ Get first element of list or None """
        return array[0] if array else None
