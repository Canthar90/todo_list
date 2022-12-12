def message_composing(todos_arg):
    """Compose message from list separating every element by newline"""
    message = ''
    for index, item in enumerate(todos_arg):
        message += (f"{index + 1}-{item.strip()}\n")
    return message
        
        
def save_to_txt(todos_arg, filepath=r"todolist\todos.txt"):
    """Saving list to txt line by line"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
        
        
if __name__ == "main":
    print("Hello")
    