import managment
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")


window = sg.Window("My To-Do APP", 
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read()
    
    print(event, values)
    match event:
        case "Add":
            todos = managment.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            managment.save_to_txt(todos)
        case sg.WIN_CLOSED:
            break
            

window.close()