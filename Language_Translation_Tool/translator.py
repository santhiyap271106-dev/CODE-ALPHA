from deep_translator import GoogleTranslator
import tkinter as tk

def translate_text():
    try:
        text=text_box.get("1.0",tk.END).strip()
        source=source_box.get().strip()
        target=target_box.get().strip()

        translated=GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        result_label.config(text=translated)

    except Exception as e:
        result_label.config(text="Invalid Language Code")

window=tk.Tk()

window.title("Language Translation Tool")
window.geometry("600x500")

title=tk.Label(
    window,
    text="Language Translation Tool",
    font=("Arial",16,"bold")
)
title.pack(pady=10)

tk.Label(window,text="Enter Text").pack()

text_box=tk.Text(window,height=5,width=50)
text_box.pack()

tk.Label(window,text="Source Language").pack()

source_box=tk.Entry(window)
source_box.pack()

tk.Label(window,text="Target Language").pack()

target_box=tk.Entry(window)
target_box.pack()

translate_button=tk.Button(
    window,
    text="Translate",
    command=translate_text
)
translate_button.pack(pady=10)

result_label=tk.Label(
    window,
    text="Translation will appear here",
    wraplength=500
)
result_label.pack(pady=20)

window.mainloop()