import functions

import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter Todo", key="todo")
add_button = gui.Button("Add")

window = gui.Window('To-Do App',
                    layout=[[label, input_box, add_button]],
                    font=('Helvetica', 22))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break


window.close()

