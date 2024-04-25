import streamlit as st

def swap_case(text):
    return text.swapcase()

def main():
    st.title('Cambio de Mayúsculas y Minúsculas')

    # Input de texto
    input_text = st.text_area('Ingresa un texto:')

    # Botón para procesar el texto
    if st.button('Procesar texto'):
        if input_text:
            output_text = swap_case(input_text)
            st.write('Texto procesado:')
            st.write(output_text)

            # Mostrar imagen de perro si se encuentra la palabra "perro"
            if "perro" in output_text.lower():
                st.markdown("---")
                st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nationalgeographic.com%2Fanimals%2Fmammals%2Ffacts%2Fdomestic-dog&psig=AOvVaw0XYdLbMdalMbYb70eEwyj4&ust=1714127016171000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCJCS__CS3YUDFQAAAAAdAAAAABAE")
                st.markdown("---")
        else:
            st.warning('Por favor ingresa un texto antes de procesar.')

if __name__ == '__main__':
    main()
