import time
import FreeSimpleGUI as gui

gui.theme("DarkTeal12")

user = gui.popup_get_text("What is your name?")
user_file = user+'.txt'

def get_todos(filepath=user_file):
    """Read a text file and return the list of t
    to dod items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=user_file):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



clock = gui.Text('', key='clock')
label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter Todo", key="todo")
add_button = gui.Button("Add")

list_box = gui.Listbox(values=get_todos(), key='todos', enable_events=True, size=(45, 10))

edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")


window = gui.Window(f"{user}'s To-Do's ",
                    layout=[[clock],
                            [label, input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 22))
while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y     %H:%M:%S"))
    match event:
        case "Add":
            todos =get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first.", font= ("Helvetica", 22))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 22))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
