import streamlit as st
import functions

todos = functions.get_todos()

def get_todo():
    new_todo = st.session_state["new_item"].title() + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)

st.title('To-Do App',)
st.subheader('This app is to increase your productivity')

st.text_input(label="Enter To Dos", placeholder="Add a new To Do",
                      on_change=get_todo, key="new_item")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

