import managment
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
main_prompt = "Type add, show, edit, complete or exit: "
user_prompt = "Type todo item: "
creating_todo = True
with open("todos.txt") as file:
    todos = file.readlines()


while creating_todo:
    
    user_action = input(main_prompt).strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos.append(todo.capitalize())
        managment.save_to_txt(todos)
        
    elif user_action.startswith("show"):   
        print(managment.message_composing(todos))
        
    elif user_action.startswith("edit"):
             
        try:
            number = int(user_action[5:])
            todos[number-1] = input(f"you are editing item: {todos[number-1]} enter new item : ") + "\n"
            print(f"item {number} succesfully changed to: {todos[number-1]}")
            managment.save_to_txt(todos)
        
        except ValueError:                
            print("Invalid value passed. Number of task expected")
            continue
            
        except IndexError:
            print("Number of task invalid. We dont have task with this number.")
            continue
    
    elif user_action.startswith("complete"):
        try:
            item_to_remove = int(user_action[9:])
            print(f"following item was removed {item_to_remove}-{todos.pop(item_to_remove-1)}")
            print(f"There are following tasks to be done:")
            print(managment.message_composing(todos))
            managment.save_to_txt(todos)
        
        except ValueError:
            print("Invalid value passed. Number of task expected.")
            continue
            
        except IndexError:
            print("Number of task invalid. We dont have task with this number.")
            continue
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("input was incorrect plis try again")

        

managment.message_composing(todos)
print("Bobayy !!")