from scripts.crud_operations.crud_operation import (
    insert_item,read_item,
    update_item,delete_item

)
from decimal import Decimal
from scripts.crud_operations.query_operation import Query_Operation
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
students=Query_Operation.high_attendance_record()
for student in students:
    print(student)
students2=Query_Operation.weekly_self_study()
for student in students2:
    print(student)

students3 =Query_Operation.get_excellent_students()
for ex in students3:
    print(ex)


       