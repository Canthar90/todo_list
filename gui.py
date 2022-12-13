import managment
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=managment.get_todos(),
                      key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

window = sg.Window("My To-Do APP", 
                   layout=[[label], [input_box, add_button], 
                           [list_box , edit_button ]],
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
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"]
            if values["todo"]:
                new_todo = values["todo"]
                todos = managment.get_todos()
                index = todos.index(todo_to_edit[0])
                todos[index] = new_todo
                managment.save_to_txt(todos)
                window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
            

window.close()