import managment
import PySimpleGUI as sg
import time
import os


if not os.path.exists(r"todos.txt"):
    with open("todos.txt", "w") as file:
        pass
    
sg.theme("Topanga")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(key="Add", image_source=r"add.png", size=2, mouseover_colors="LightBlue2",
                       tooltip="Add Todo")
list_box = sg.Listbox(values=managment.get_todos(),
                      key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do APP", 
                   layout=[[clock],
                            [label], [input_box, add_button], 
                           [list_box , edit_button,complete_button ],
                           [exit_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read(timeout=800)
    window['clock'].update(value=time.strftime("%b-%d, %Y-%H:%M:%S"))
    
    match event:
        case "Add":
            todos = managment.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            managment.save_to_txt(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"]
            
                new_todo = values["todo"]
                todos = managment.get_todos()
                index = todos.index(todo_to_edit[0])
                todos[index] = new_todo
                managment.save_to_txt(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup_annoying("Plis select todo item to edit")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = managment.get_todos()
                todos.remove(todo_to_complete)
                managment.save_to_txt(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup_annoying("Plis select todo item to complete")
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
            

window.close()