import tkinter as tk

# Diccionario para la traducción de letras, números y signos a código Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Función para traducir texto a código Morse
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += '[INVALID] '
    return morse_code

# Función para traducir código Morse a texto
def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if value == code:
                text += key
                break
        else:
            text += '[INVALID]'
    return text

# Función para manejar el evento del botón de traducción
def translate():
    input_text = entry.get()
    if '-' in input_text or '.' in input_text:
        translated_text = morse_to_text(input_text)
    else:
        translated_text = text_to_morse(input_text)
    result_label.config(text="Resultado: " + translated_text)

# Crear la ventana principal
root = tk.Tk()
root.title("Traductor Morse")

# Crear y posicionar los elementos de la interfaz
label = tk.Label(root, text="Introduce texto o código Morse:")
label.pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
translate_button = tk.Button(root, text="Traducir", command=translate)
translate_button.pack(pady=5)
result_label = tk.Label(root, text="Resultado: ")
result_label.pack(pady=5)

# Ejecutar el bucle principal de la interfaz
root.mainloop()
