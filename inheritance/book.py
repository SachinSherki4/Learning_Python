'''
Created on Oct 28, 2024

@author: ssherki
'''
from inheritance.product import Product

class Book(Product):
    def __init__(self, name, price, sku, author, pages):
        super().__init__(name, price, sku)
        self.author = author
        self.pages = pages
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Author: {self.author}, Total Pages: {self.pages}"
    
    