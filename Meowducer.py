import sys
import tkinter as tk
from tkinter import messagebox
# Meowducer - Feline-themed text cipher tool
# Copyright (C) 2026 Redcat 607
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# version 2.5.2

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789 .,!?'"
SOUNDS = ["mew", "meow", "prr", "purr"]
SOUND_TO_VAL = {sound: i for i, sound in enumerate(SOUNDS)}


def encode_meow(text: str) -> str:
    text = text.lower()
    encoded_words = []
    for char in text:
        if char not in ALPHABET:
            continue
        val = ALPHABET.index(char)
        d1 = val // 16
        d2 = (val % 16) // 4
        d3 = val % 4
        encoded_words.extend([SOUNDS[d1], SOUNDS[d2], SOUNDS[d3]])
    return " ".join(encoded_words)


def decode_meow(cat_text: str) -> str:
    words = cat_text.strip().split()
    if not words:
        return ""
    if len(words) % 3 != 0:
        return "⚠️ Error: The cat message is incomplete (must be a multiple of 3 words)."

    decoded_chars = []
    for i in range(0, len(words), 3):
        w1, w2, w3 = words[i], words[i + 1], words[i + 2]
        if (
            w1 not in SOUND_TO_VAL
            or w2 not in SOUND_TO_VAL
            or w3 not in SOUND_TO_VAL
        ):
            return (
                f"⚠️ Error: Unrecognized meow ('{w1}', '{w2}' or '{w3}')."
            )

        d1, d2, d3 = SOUND_TO_VAL[w1], SOUND_TO_VAL[w2], SOUND_TO_VAL[w3]
        val = (d1 * 16) + (d2 * 4) + d3
        if val < len(ALPHABET):
            decoded_chars.append(ALPHABET[val])

    return "".join(decoded_chars)


def show_help():
    help_text = """
    Meowducer v2.5.2

Usage:
  python meowducer.py [OPTION] [TEXT]

Command options:
  -h, --h, --help       Displays this help menu and exits.
  -c, --console         Starts the program in interactive console mode.
  -e, --encode [text]   Encodes the provided text into meowscript directly.
  -d, --decode [text]   Decodes the provided meowscript into text directly.

No options:
  Running the script without arguments will open the Graphical User Interface (GUI).

Cipher details:
  - Supported alphabet: Letters (a-z), numbers (0-9), spaces, and characters: . , ! ? '
  - Sounds used: mew (0), meow (1), prr (2), purr (3)
  - Encoding chain: Each character equals 3 meows.
"""
    print(help_text)
    sys.exit()


def run_console_mode():
    print("\n Meowducer v2.5.2")
    while True:
        print("\n1. Text -> Meowscript")
        print("2. Meowscript -> Text")
        print("3. Exit")
        opt = input("\n> ").strip()

        if opt == "1":
            print("\n" + encode_meow(input("Text: ")))
        elif opt == "2":
            print("\n" + decode_meow(input("Meowscript: ")))
        elif opt == "3":
            sys.exit()


if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if arg in ("-h", "--h", "--help", "-help"):
        show_help()
    elif arg in ("-c", "--console"):
        run_console_mode()
    elif arg in ("-e", "--encode"):
        if len(sys.argv) > 2:
            print(encode_meow(" ".join(sys.argv[2:])))
        else:
            print("⚠️ Error: Please provide text to encode.")
        sys.exit()
    elif arg in ("-d", "--decode"):
        if len(sys.argv) > 2:
            print(decode_meow(" ".join(sys.argv[2:])))
        else:
            print("⚠️ Error: Please provide meowscript to decode.")
        sys.exit()


def btn_encode_click():
    input_text = txt_normal.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showinfo(
            "Notice", "Write something in the normal text box."
        )
        return
    result = encode_meow(input_text)
    txt_meow.delete("1.0", tk.END)
    txt_meow.insert(tk.END, result)


def btn_decode_click():
    input_meow = txt_meow.get("1.0", tk.END).strip()
    if not input_meow:
        messagebox.showinfo(
            "Notice", "Paste the cat code in the bottom box."
        )
        return
    result = decode_meow(input_meow)
    txt_normal.delete("1.0", tk.END)
    txt_normal.insert(tk.END, result)


def btn_clear_click():
    txt_normal.delete("1.0", tk.END)
    txt_meow.delete("1.0", tk.END)


root = tk.Tk()
root.title("Meowducer v2.5.2 🐾")
root.geometry("640x620")
root.configure(bg="#1A1826")

FONT_LABEL = ("Segoe UI", 12, "bold")
FONT_TEXT = ("Consolas", 11)


lbl_title = tk.Label(
    root,
    text="✨ Meowducer ✨",
    font=("Segoe UI", 20, "bold"),
    fg="#F5C2E7",
    bg="#1A1826",
)
lbl_title.pack(pady=15)


frame_normal = tk.Frame(root, bg="#1A1826")
frame_normal.pack(fill="both", expand=True, padx=25, pady=5)

lbl_normal = tk.Label(
    frame_normal, text="Human Text", font=FONT_LABEL, fg="#B4BEFE", bg="#1A1826"
)
lbl_normal.pack(anchor="w", pady=(0, 5))

txt_normal = tk.Text(
    frame_normal,
    height=5,
    font=FONT_TEXT,
    bg="#302D41",
    fg="#D9E0EE",
    insertbackground="#F5C2E7",
    wrap="word",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#575268",
    highlightcolor="#B4BEFE",
    padx=10,
    pady=10,
)
txt_normal.pack(fill="both", expand=True)


frame_buttons = tk.Frame(root, bg="#1A1826")
frame_buttons.pack(pady=15)

btn_encode = tk.Button(
    frame_buttons,
    text="Meow it 🐾",
    font=FONT_LABEL,
    bg="#F38BA8",
    fg="#161320",
    activebackground="#EBA0AC",
    command=btn_encode_click,
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
)
btn_encode.grid(row=0, column=0, padx=10)

btn_decode = tk.Button(
    frame_buttons,
    text="Text it 💬",
    font=FONT_LABEL,
    bg="#89B4FA",
    fg="#161320",
    activebackground="#B4BEFE",
    command=btn_decode_click,
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
)
btn_decode.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(
    frame_buttons,
    text="Clear ❌",
    font=FONT_LABEL,
    bg="#F5C2E7",
    fg="#161320",
    activebackground="#F4B8E4",
    command=btn_clear_click,
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
)
btn_clear.grid(row=0, column=2, padx=10)


frame_meow = tk.Frame(root, bg="#1A1826")
frame_meow.pack(fill="both", expand=True, padx=25, pady=5)

lbl_meow = tk.Label(
    frame_meow,
    text="Meowscript",
    font=FONT_LABEL,
    fg="#F2CDCD",
    bg="#1A1826",
)
lbl_meow.pack(anchor="w", pady=(0, 5))

txt_meow = tk.Text(
    frame_meow,
    height=5,
    font=FONT_TEXT,
    bg="#302D41",
    fg="#F2CDCD",
    insertbackground="#F38BA8",
    wrap="word",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#575268",
    highlightcolor="#F38BA8",
    padx=10,
    pady=10,
)
txt_meow.pack(fill="both", expand=True)


lbl_version = tk.Label(
    root,
    text="v2.5.2",
    font=("Segoe UI", 9, "bold"),
    fg="#6E6C7E",
    bg="#1A1826",
)
lbl_version.pack(side="bottom", pady=12)

root.mainloop()