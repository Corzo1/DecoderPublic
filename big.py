from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from base64 import b64decode


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "rb") as file:
            file_contents = file.read()
            decoded_contents = decode_input(file_contents)
            show_decoded_text(decoded_contents)


def show_text_input():
    text_input = Toplevel(root)
    text_input.title("Enter Text")
    text_input.geometry("300x300")
    text_input.resizable(True, True)

    text_input_label = Label(text_input, text="Enter text to decode:")
    text_input_label.pack(pady=10)

    text_box = Text(text_input, height=10, width=30)
    text_box.pack(pady=5)

    decode_button = Button(text_input, text="Decode Text",
                           command=lambda: on_decode_text(text_box.get("1.0", END)))
    decode_button.pack(pady=10)

    text_input.mainloop()


def on_decode_text(input_str):
    decoded_contents = decode_input(input_str)
    show_decoded_text(decoded_contents)


def decode_input(input_str):
    try:
        decoded_input = b64decode(input_str).decode()
        return decoded_input
    except Exception as e:
        messagebox.showerror("Error", f"Error decoding input: {e}")
        return None


def show_decoded_text(decoded_contents):
    if decoded_contents is not None:
        decoded_text_window = Toplevel(root)
        decoded_text_window.title("Decoded Text")
        decoded_text_window.geometry("400x300")
        decoded_text_window.resizable(True, True)

        decoded_text_label = Label(decoded_text_window, text="Decoded Text:")
        decoded_text_label.pack(pady=10)

        decoded_text = Text(decoded_text_window, height=100, width=250)
        decoded_text.pack(pady=5)

        decoded_text.insert(END, decoded_contents)
        decoded_text.configure(state="disabled")

        copy_button = Button(decoded_text_window, text="Copy to Clipboard",
                             command=lambda: root.clipboard_append(decoded_contents))
        copy_button.pack(pady=10)

        decoded_text_window.mainloop()


root = Tk()
root.title("Base64 Decoder")
root.geometry("150x150")
root.resizable(False, False)

file_button = Button(root, text="Select File", command=select_file)
file_button.pack(pady=10)

text_button = Button(root, text="Enter Text", command=show_text_input)
text_button.pack(pady=10)

root.mainloop()
