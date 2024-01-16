#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand
    # @property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Refer to this YT video for further explanation https://youtu.be/Sz9G0iwwHQI?si=gEaLS5iCkCLiJ9UJ
      
    # Getter Method
    @property
    def size(self):
        # In Python, by convention, when you add a leading underscore to a name (self._size in this case), you are telling other developers that it should not be accessed or modified directly outside of the class. It should only be accessed through intermediaries (getters and setters) if they are available.
        return self._size
    
    # Setter Method
    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")