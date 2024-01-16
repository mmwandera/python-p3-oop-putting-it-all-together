#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

     # @property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Refer to this YT video for further explanation https://youtu.be/Sz9G0iwwHQI?si=gEaLS5iCkCLiJ9UJ
    @property
    def page_count(self):
        # In Python, by convention, when you add a leading underscore to a name (self._page_count in this case), you are telling other developers that it should not be accessed or modified directly outside of the class. It should only be accessed through intermediaries (getters and setters) if they are available.
        return self._page_count
    
    # Setter Method
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        