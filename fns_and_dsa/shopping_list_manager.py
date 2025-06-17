# shopping_list_manager.py
def add_item(item):
    shopping_list.append(item)
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
def view_list():
    if not shopping_list:
        return "Your shopping list is empty."
    return shopping_list
