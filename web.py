import streamlit as st
import managment


todos = managment.get_todos()

st.title("Tasks list App")
st.subheader("This im my todo/tasks app")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Input new todo....")
