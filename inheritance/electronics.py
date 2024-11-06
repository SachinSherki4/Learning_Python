'''
Created on Oct 28, 2024

@author: ssherki
'''
from inheritance.product import Product

class Electronics(Product):
    
    def __init__(self,name,price,sku,warrenty_period):
        super().__init__(name,price,sku)
        self.warrenty_period=warrenty_period
    
    def display_info(self):
        base_info=super().display_info()
        return f"{base_info}, Warrenty Period : {self.warrenty_period} Years"
    