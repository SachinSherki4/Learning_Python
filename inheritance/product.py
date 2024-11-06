'''
Created on Oct 28, 2024

@author: ssherki
'''

class Product(object):
    
    def __init__(self,name,price,sku):
         self.name=name
         self.price=price
         self.sku=sku 
    def display_info(self):
        return f"Product : {self.name}, Price : {self.price:.2f}, SKU : {self.sku}"
    
    def apply_discount(self,discount_percent):
        discount_amount= self.price * (discount_percent/100)
        self.price -= discount_amount
        return f"New Price after discount {self.price:.2f}"
        
