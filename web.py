import streamlit as st
import managment


if not os.path.exists(r"todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = managment.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo.strip():
        todos.append(todo)
        managment.save_to_txt(todos)
    

st.title("Tasks list App")
st.subheader("This im my todo/tasks app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):

    checkbox = st.checkbox(todo, key=index )
    if checkbox:
        todos.pop(index)
        managment.save_to_txt(todos)
        del st.session_state[index]
        st.experimental_rerun()
    


st.text_input(label=" ", placeholder="Input new todo....",
              on_change=add_todo, key="new_todo")



st.write("Created by Dawid Cieślak")