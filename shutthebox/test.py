my_list = ["apple", "banana", "cherry", "orange"]

item_to_remove = input("Enter the item to remove: ")

if item_to_remove in my_list:
  my_list.remove(item_to_remove)
  print(f"Removed item: {item_to_remove}")
else:
  print(f"{item_to_remove} not found in the list.")

print("Updated list:", my_list)
