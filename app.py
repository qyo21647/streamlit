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
        else:
            st.warning('Por favor ingresa un texto antes de procesar.')

if __name__ == '__main__':
    main()
