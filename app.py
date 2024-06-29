import streamlit as st

st.set_page_config(
    page_title="Duoc UC Deportes",
    page_icon=":sports_medal:",
    layout="wide",
)

# Header 
st.markdown("<h1 style='text-align: center; color: #f29820;'>Duoc UC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Universidad de Artes, Ciencias y Tecnologías</p>", unsafe_allow_html=True)

# Navigation bar
st.sidebar.markdown("<h3 style='text-align: center;'>Navigation</h3>", unsafe_allow_html=True)
st.sidebar.write("[Alumnos](https://www.duoc.cl/alumnos/)", unsafe_allow_html=True)
st.sidebar.write("[Titulados](https://www.duoc.cl/titulados/)", unsafe_allow_html=True)
st.sidebar.write("[Docentes](https://www.duoc.cl/docentes/)", unsafe_allow_html=True)
st.sidebar.write("[Colaboradores](https://www.duoc.cl/colaboradores/)", unsafe_allow_html=True)
st.sidebar.write("[AVA](https://www.duoc.cl/ava/)", unsafe_allow_html=True)
st.sidebar.write("[Empresas](https://www.duoc.cl/empresas/)", unsafe_allow_html=True)
st.sidebar.write("[Biblioteca](https://www.duoc.cl/biblioteca/)", unsafe_allow_html=True)
st.sidebar.write("[Liceo Andes](https://www.duoc.cl/liceo-andes/)", unsafe_allow_html=True)
st.sidebar.write("[Dónde estamos](https://www.duoc.cl/donde-estamos/)", unsafe_allow_html=True)
st.sidebar.write("[Pago en línea](https://www.duoc.cl/pago-en-linea/)", unsafe_allow_html=True)
st.sidebar.write("[Contacto](https://www.duoc.cl/contacto/)", unsafe_allow_html=True)
st.sidebar.write("[Certificados](https://www.duoc.cl/certificados/)", unsafe_allow_html=True)
st.sidebar.write("[Matrícula Duoc Online](https://www.duoc.cl/matricula-duoc-online/)", unsafe_allow_html=True)
st.sidebar.write("[Oferta Académica](https://www.duoc.cl/oferta-academica/)", unsafe_allow_html=True)
st.sidebar.write("[Vida Estudiantil](https://www.duoc.cl/vida-estudiantil/)", unsafe_allow_html=True)
st.sidebar.write("[Extensión](https://www.duoc.cl/extension/)", unsafe_allow_html=True)
st.sidebar.write("[Noticias y Eventos](https://www.duoc.cl/noticias-y-eventos/)", unsafe_allow_html=True)
st.sidebar.write("[Nosotros](https://www.duoc.cl/nosotros/)", unsafe_allow_html=True)
st.sidebar.write("[Admisión](https://www.duoc.cl/admision/)", unsafe_allow_html=True)


# Main content
# Image 
st.image("https://www.duoc.cl/wp-content/uploads/2023/02/duoc-uc-deportes.jpg", caption="Deportes Duoc UC")

# Title 
st.markdown("<h2 style='text-align: center; color: #f29820;'>Deportes</h2>", unsafe_allow_html=True)

# Navigation links
st.markdown("<p style='text-align: center;'>Inicio / Vida Estudiantil / Deportes</p>", unsafe_allow_html=True)

# Main sections
st.markdown("<h3 style='text-align: center; color: #f29820;'>Nuestra oferta deportiva</h3>", unsafe_allow_html=True)

# Content
st.markdown("<p style='text-align: center;'>En Duoc UC, te invitamos a vivir una experiencia deportiva única, con una oferta completa que te permitirá desarrollar tus habilidades, disfrutar del deporte y fortalecer tu salud. Te invitamos a explorar nuestras ramas deportivas, selecciones, juegos de invierno, juegos olímpicos y coordinadores por sede. ¡Anímate a ser parte de nuestro equipo!</p>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)

# Links
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Ramas Deportivas", style="primary", help="Ir a Ramas Deportivas", on_click=lambda: webbrowser.open("https://www.duoc.cl/ramas-deportivas/"))

with col2:
    st.button("Selecciones", style="primary", help="Ir a Selecciones", on_click=lambda: webbrowser.open("https://www.duoc.cl/selecciones/"))

with col3:
    st.button("Juegos de Invierno", style="primary", help="Ir a Juegos de Invierno", on_click=lambda: webbrowser.open("https://www.duoc.cl/juegos-de-invierno/"))

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Juegos Olímpicos", style="primary", help="Ir a Juegos Olímpicos", on_click=lambda: webbrowser.open("https://www.duoc.cl/juegos-olimpicos/"))

with col2:
    st.button("Coordinadores por Sede", style="primary", help="Ir a Coordinadores por Sede", on_click=lambda: webbrowser.open("https://www.duoc.cl/coordinadores-por-sede/"))

with col3:
    st.button("Noticias", style="primary", help="Ir a Noticias", on_click=lambda: webbrowser.open("https://www.duoc.cl/noticias/"))

st.write("")

st.button("Galerías", style="primary", help="Ir a Galerías", on_click=lambda: webbrowser.open("https://www.duoc.cl/galerias/"))

# Footer copyright
st.markdown("<p style='text-align: center;'>© 2023 Duoc UC. Todos los derechos reservados.</p>", unsafe_allow_html=True)
