import streamlit as st


def main():
    st.title("Detección de Marcas")

    

    # Aquí puedes agregar elementos interactivos, como botones, selectores, etc.
    st.sidebar.header("Configuración")
    # Agrega elementos interactivos a la barra lateral o al cuerpo principal

    # Puedes cargar y mostrar imágenes
    uploaded_image = st.file_uploader(
        "Subir imagen", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Imagen cargada.",
                 use_column_width=True)

    # Puedes mostrar resultados, gráficos, etc.
    st.subheader("Resultados")

    # Aquístreamlit run app.py puedes agregar más contenido según las necesidades de tu proyecto


if __name__ == "__main__":
    main()
