import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mi pagina", page_icon=":technologist:")

st.title("Deportes")

with st.sidebar:
    seleccionado=option_menu(
    menu_title=None,
    options= ["Alumnos","Titulados","Docentes","Colaboradores","AVA","Empresas","Biblioteca","Liceo Andes",""],
    )
if seleccionado=="Alumnos":
    st
elif seleccionado=="Titulados":
    st
st.write("""""")