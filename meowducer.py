import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from math import cos, pi, sin
import time
# Meowducer - Feline-themed text cipher tool
# Copyright (C) 2026 Redcat 607
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# version 2.6.0

VERSION = "2.6.0"
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789 .,!?'"
SOUNDS = ["mew", "meow", "prr", "purr"]
SOUND_TO_VAL = {sound: i for i, sound in enumerate(SOUNDS)}


def encode_meow(text: str, salt: str = "") -> str:
    text = text.lower()
    salt_values = [ord(char) % len(ALPHABET) for char in salt]
    salt_position = 0
    encoded_words = []
    for char in text:
        if char not in ALPHABET:
            continue
        val = ALPHABET.index(char)
        if salt_values:
            val = (val + salt_values[salt_position % len(salt_values)]) % len(ALPHABET)
            salt_position += 1
        d1 = val // 16
        d2 = (val % 16) // 4
        d3 = val % 4
        encoded_words.extend([SOUNDS[d1], SOUNDS[d2], SOUNDS[d3]])
    return " ".join(encoded_words)


def decode_meow(cat_text: str, salt: str = "") -> str:
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

    salt_values = [ord(char) % len(ALPHABET) for char in salt]
    if salt_values:
        decoded_chars = [
            ALPHABET[(ALPHABET.index(char) - salt_values[index % len(salt_values)]) % len(ALPHABET)]
            for index, char in enumerate(decoded_chars)
        ]

    return "".join(decoded_chars)


def show_help():
    help_text = f"""
    Meowducer v{VERSION}

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
    print(f"\n Meowducer v{VERSION}")
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
    result = encode_meow(input_text, txt_salt.get())
    txt_meow.delete("1.0", tk.END)
    txt_meow.insert(tk.END, result)


def btn_decode_click():
    input_meow = txt_meow.get("1.0", tk.END).strip()
    if not input_meow:
        messagebox.showinfo(
            "Notice", "Paste the cat code in the bottom box."
        )
        return
    result = decode_meow(input_meow, txt_salt.get())
    txt_normal.delete("1.0", tk.END)
    txt_normal.insert(tk.END, result)


def btn_clear_click():
    txt_normal.delete("1.0", tk.END)
    txt_meow.delete("1.0", tk.END)

def copy_text(widget):
    texto_a_copiar = widget.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(texto_a_copiar)
    root.update()


def paste_text(widget):
    try:
        clipboard_text = root.clipboard_get()
    except tk.TclError:
        return
    widget.insert(tk.INSERT, clipboard_text)
    widget.focus_set()


def rounded_button(parent, text, command, bg, fg, active_bg, font, padx, pady):
    button_font = tkfont.Font(root=parent, font=font)
    width = button_font.measure(text) + (padx * 2)
    height = button_font.metrics("linespace") + (pady * 2)
    radius = min(8, height / 2)
    points = []
    corners = (
        (width - radius, radius, -90),
        (width - radius, height - radius, 0),
        (radius, height - radius, 90),
        (radius, radius, 180),
    )
    for center_x, center_y, start_angle in corners:
        for step in range(7):
            angle = (start_angle + step * 15) * pi / 180
            points.extend((center_x + radius * cos(angle),
                           center_y + radius * sin(angle)))

    button = tk.Canvas(
        parent,
        width=width,
        height=height,
        bg=BG,
        highlightthickness=0,
        takefocus=True,
        cursor="hand2",
    )
    shape = button.create_polygon(points, fill=bg, outline=bg)
    button.create_text(
        width / 2,
        height / 2,
        text=text,
        font=button_font,
        fill=fg,
    )
    button.bind(
        "<Enter>",
        lambda event: button.itemconfigure(shape, fill=active_bg, outline=active_bg),
    )
    button.bind(
        "<Leave>",
        lambda event: button.itemconfigure(shape, fill=bg, outline=bg),
    )
    button.bind("<Button-1>", lambda event: command())
    button.bind("<Return>", lambda event: command())
    button.bind("<space>", lambda event: command())
    return button


root = tk.Tk()
root.title(f"Meowducer v{VERSION}")
root.geometry("640x680")
root.configure(bg="#111111")

BG = "#111111"
FIELD_BG = "#1D1B1B"
TEXT_FG = "#F2EEEE"
MUTED_FG = "#A99595"
ACCENT = "#D94343"
FONT_LABEL = ("Segoe UI", 11, "bold")
FONT_TEXT = ("Consolas", 11)


header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=25, pady=(12, 8))

lbl_title = tk.Label(
    header,
    text="Meowducer",
    font=("Segoe UI", 19, "bold"),
    fg="#F0DADA",
    bg=BG,
)
lbl_title.pack(side="left")

salt_frame = tk.Frame(header, bg=BG)
salt_frame.pack(side="right")

lbl_salt = tk.Label(
    salt_frame,
    text="Salt (optional)",
    font=("Segoe UI", 9, "bold"),
    fg=MUTED_FG,
    bg=BG,
)
lbl_salt.pack(anchor="e", pady=(0, 3))

txt_salt = tk.Entry(
    salt_frame,
    width=18,
    font=("Consolas", 10),
    bg=FIELD_BG,
    fg=TEXT_FG,
    insertbackground=ACCENT,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#4A2929",
    highlightcolor=ACCENT,
)
txt_salt.pack()


frame_normal = tk.Frame(root, bg=BG)
frame_normal.pack(fill="both", expand=True, padx=25, pady=(4, 2))

lbl_normal = tk.Label(
    frame_normal,
    text="Decrypted text",
    font=FONT_LABEL,
    fg=TEXT_FG,
    bg=BG,
)
lbl_normal.pack(anchor="w", pady=(0, 5))

txt_normal = tk.Text(
    frame_normal,
    height=5,
    font=FONT_TEXT,
    bg=FIELD_BG,
    fg=TEXT_FG,
    insertbackground=ACCENT,
    wrap="word",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#4A2929",
    highlightcolor=ACCENT,
    padx=10,
    pady=10,
)
txt_normal.pack(fill="both", expand=True)

normal_actions = tk.Frame(frame_normal, bg=BG)
normal_actions.pack(anchor="e", pady=(6, 0))

btn_copy_normal = rounded_button(
    normal_actions,
    "Copy",
    lambda: copy_text(txt_normal),
    "#302626",
    TEXT_FG,
    "#4A2C2C",
    ("Segoe UI", 9),
    9,
    3,
)
btn_copy_normal.pack(side="left", padx=(0, 6))

btn_paste_normal = rounded_button(
    normal_actions,
    "Paste",
    lambda: paste_text(txt_normal),
    "#302626",
    TEXT_FG,
    "#4A2C2C",
    ("Segoe UI", 9),
    9,
    3,
)
btn_paste_normal.pack(side="left")


frame_buttons = tk.Frame(root, bg=BG)
frame_buttons.pack(pady=10)

btn_encode = rounded_button(
    frame_buttons,
    "Encrypt",
    btn_encode_click,
    "#C93636",
    "#FFFFFF",
    "#E04A4A",
    FONT_LABEL,
    15,
    8,
)
btn_encode.grid(row=0, column=0, padx=10)

btn_decode = rounded_button(
    frame_buttons,
    "Decrypt",
    btn_decode_click,
    "#702D32",
    "#FFFFFF",
    "#8C383E",
    FONT_LABEL,
    15,
    8,
)
btn_decode.grid(row=0, column=1, padx=10)

btn_clear = rounded_button(
    frame_buttons,
    "Clear all",
    btn_clear_click,
    "#302626",
    TEXT_FG,
    "#4A2C2C",
    FONT_LABEL,
    15,
    8,
)
btn_clear.grid(row=0, column=2, padx=10)



frame_meow = tk.Frame(root, bg=BG)
frame_meow.pack(fill="both", expand=True, padx=25, pady=(2, 4))

lbl_meow = tk.Label(
    frame_meow,
    text="Encrypted text",
    font=FONT_LABEL,
    fg=TEXT_FG,
    bg=BG,
)
lbl_meow.pack(anchor="w", pady=(0, 5))

txt_meow = tk.Text(
    frame_meow,
    height=5,
    font=FONT_TEXT,
    bg=FIELD_BG,
    fg=TEXT_FG,
    insertbackground=ACCENT,
    wrap="word",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#4A2929",
    highlightcolor=ACCENT,
    padx=10,
    pady=10,
)
txt_meow.pack(fill="both", expand=True)

meow_actions = tk.Frame(frame_meow, bg=BG)
meow_actions.pack(anchor="e", pady=(6, 0))

btn_copy_meow = rounded_button(
    meow_actions,
    "Copy",
    lambda: copy_text(txt_meow),
    "#302626",
    TEXT_FG,
    "#4A2C2C",
    ("Segoe UI", 9),
    9,
    3,
)
btn_copy_meow.pack(side="left", padx=(0, 6))

btn_paste_meow = rounded_button(
    meow_actions,
    "Paste",
    lambda: paste_text(txt_meow),
    "#302626",
    TEXT_FG,
    "#4A2C2C",
    ("Segoe UI", 9),
    9,
    3,
)
btn_paste_meow.pack(side="left")


lbl_version = tk.Label(
    root,
    text=f"v{VERSION}",
    font=("Segoe UI", 9, "bold"),
    fg=MUTED_FG,
    bg=BG,
)
lbl_version.pack(side="bottom", pady=12)

root.mainloop()