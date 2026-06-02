from scripts.crud_operations.crud_operation import (
    insert_item,read_item,
    update_item,delete_item

)
from decimal import Decimal

while True:

    print("\n1. Insert")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    k = int(input("Enter your choice: "))

    if k == 1:
        insert_item()
    elif k == 2:
        read_item()
    elif k == 3:
        update_item()
    elif k==4:
        delete_item()
    else:
        break
       