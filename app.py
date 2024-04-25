import streamlit as st
from rich.console import Console

def swap_case(text):
    return text.swapcase()

def main():
    st.title('Cambio de Mayúsculas y Minúsculas')

    # Input de texto
    input_text = st.text_area('Ingresa un texto:')

    # Botón para procesar el texto
    if st.button('Procesar texto'):
        if input_text:
            console = Console()
            output_text = swap_case(input_text)
            # Separar el texto en símbolos y palabras
            words = output_text.split()
            symbols = [char for word in words for char in word if not char.isalnum()]
            text_without_symbols = ''.join(word for word in words if word.isalnum())

            # Colorear los símbolos en rojo
            for symbol in symbols:
                text_without_symbols = text_without_symbols.replace(symbol, console.render(symbol, style="red"))

            st.write('Texto procesado:')
            st.write(text_without_symbols)
        else:
            st.warning('Por favor ingresa un texto antes de procesar.')

if __name__ == '__main__':
    main()
