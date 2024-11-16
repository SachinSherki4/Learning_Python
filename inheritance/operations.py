'''
Created on Oct 28, 2024

@author: ssherki
'''
import time
from inheritance.electronics import Electronics
from inheritance.clothing import Clothing
from inheritance.book import Book

print("Execution Started! \n")
start_time=time.time()
# create instance of books, clothings, electronics 
book1 = Book("1984", 15.99, "B001", "George Orwell", 328)
laptop = Electronics("Laptop", 999.99, "E001", 2)
shirt = Clothing("T-Shirt", 19.99, "C001", "L", "Cotton")

#store them in list
products=[book1,laptop,shirt]

#display information of each product
for product in products :
    print(product.display_info())
    print(product.apply_discount(0.05))
    print()


print("\nExecution Ended")
time.sleep(0.1)
end_time=time.time()
print(f"Total Execution Time of this code including extra 0.1 seconds : {end_time-start_time-0.1} seconds")