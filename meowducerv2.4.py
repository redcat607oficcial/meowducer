import sys
import tkinter as tk
from tkinter import messagebox
# version 2.5
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
    Meowducer v2.5

Usage:
  python meowducer.py [OPTION]

Command options:
  -h, --h, --help    Displays this help menu and exits.
  -c, --console      Starts the program in interactive console mode.

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
    print("\n Meowducer v2.5")
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
root.title("Meowducer v2.5")
root.geometry("620x580")
root.configure(bg="#1E1E2E")

FONT_LABEL = ("Segoe UI", 11, "bold")
FONT_TEXT = ("Consolas", 11)


lbl_title = tk.Label(
    root,
    text="Meowducer",
    font=("Segoe UI", 16, "bold"),
    fg="#FF9ECD",
    bg="#1E1E2E",
)
lbl_title.pack(pady=12)


frame_normal = tk.Frame(root, bg="#1E1E2E")
frame_normal.pack(fill="both", expand=True, padx=20, pady=5)

lbl_normal = tk.Label(
    frame_normal, text="Text", font=FONT_LABEL, fg="#CDD6F4", bg="#1E1E2E"
)
lbl_normal.pack(anchor="w")

txt_normal = tk.Text(
    frame_normal,
    height=5,
    font=FONT_TEXT,
    bg="#313244",
    fg="#CDD6F4",
    insertbackground="white",
    wrap="word",
    relief="flat",
)
txt_normal.pack(fill="both", expand=True, pady=5)


frame_buttons = tk.Frame(root, bg="#1E1E2E")
frame_buttons.pack(pady=10)

btn_encode = tk.Button(
    frame_buttons,
    text="Meow it",
    font=FONT_LABEL,
    bg="#F38BA8",
    fg="#11111B",
    activebackground="#EBA0AC",
    command=btn_encode_click,
    padx=12,
    pady=6,
    relief="flat",
    cursor="hand2",
)
btn_encode.grid(row=0, column=0, padx=6)

btn_decode = tk.Button(
    frame_buttons,
    text="Text it",
    font=FONT_LABEL,
    bg="#89B4FA",
    fg="#11111B",
    activebackground="#B4BEFE",
    command=btn_decode_click,
    padx=12,
    pady=6,
    relief="flat",
    cursor="hand2",
)
btn_decode.grid(row=0, column=1, padx=6)

btn_clear = tk.Button(
    frame_buttons,
    text="Clear",
    font=FONT_LABEL,
    bg="#6C7086",
    fg="#FFFFFF",
    activebackground="#585B70",
    command=btn_clear_click,
    padx=10,
    pady=6,
    relief="flat",
    cursor="hand2",
)
btn_clear.grid(row=0, column=2, padx=6)


frame_meow = tk.Frame(root, bg="#1E1E2E")
frame_meow.pack(fill="both", expand=True, padx=20, pady=5)

lbl_meow = tk.Label(
    frame_meow,
    text="Meowscript",
    font=FONT_LABEL,
    fg="#A6E3A1",
    bg="#1E1E2E",
)
lbl_meow.pack(anchor="w")

txt_meow = tk.Text(
    frame_meow,
    height=5,
    font=FONT_TEXT,
    bg="#313244",
    fg="#A6E3A1",
    insertbackground="white",
    wrap="word",
    relief="flat",
)
txt_meow.pack(fill="both", expand=True, pady=5)


lbl_version = tk.Label(
    root,
    text="v2.5",
    font=("Segoe UI", 9),
    fg="#6C7086",
    bg="#1E1E2E",
)
lbl_version.pack(side="bottom", pady=8)

root.mainloop()