import streamlit as st
import managment


todos = managment.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    managment.save_to_txt(todos)
    
    
# def generate_todos():
#     for todo in todos:
#         st.checkbox(todo)


st.title("Tasks list App")
st.subheader("This im my todo/tasks app")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)


st.text_input(label=" ", placeholder="Input new todo....",
              on_change=add_todo, key="new_todo")


