'''
Created on Oct 28, 2024

@author: ssherki
'''
from .product import Product

class Clothing(Product):
    def __init__(self,name,price,sku,size,fabric):
        super().__init__(name,price,sku)
        self.size=size
        self.fabric=fabric
    
    def display_info(self):
        base_info=super().display_info()
        return f"{base_info}, Size : {self.size}, Fabric Used : {self.fabric}"
    
    