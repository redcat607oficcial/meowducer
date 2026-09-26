# Meowducer 🐾
Meowducer v2.6.0 is a feline-themed Python text cipher tool. It translates text into "Meowscript" 
using a Base-4 algorithm (mew, meow, prr, purr). 
It features a black-and-red Tkinter GUI, an interactive CLI, and direct terminal commands.

---

## ✨ Features

- **Base-4 Cipher Encoding**: Translates characters into distinct 3-sound combinations using `mew`, `meow`, `prr`, and `purr`.
- **Versatile Execution Modes**:
  - 🎨 **GUI Mode**: A black-and-red interface with Encrypt, Decrypt, Copy, and Paste controls.
  - 💻 **Console Mode**: Interactive CLI mode (`-c`) for lightweight setups or terminal environments.
  - ⚡ **Direct CLI Execution**: Quickly encode (`-e`) or decode (`-d`) directly from your terminal prompt.
- **Expanded Alphabet Support**: Full support for standard English lowercase letters (`a-z`), **numbers (`0-9`)**, spaces, and basic punctuation (`. , ! ? '`).
- **Optional Salt**: The GUI can use a salt string to shift characters before encoding. Enter the same salt to decrypt; leaving it blank keeps the original behavior.

The salt feature is part of this custom cipher and is not suitable for protecting sensitive data.

---

## 🛠️ Requirements

- **Python 3.x**
- **Tkinter** 

---

## 🚀 Usage

Running the script without arguments will open the **Graphical User Interface (GUI)**:
```bash
python meowducer.py
```

## 📦 Downloadable Executables

The GitHub Actions workflow builds a Windows `.exe` and a Linux executable on every push. To build them manually, open the repository's **Actions** tab and run **Build executables**. Download `meowducer-windows-x64` or `meowducer-linux-x64` from the completed workflow run's artifacts.

The builds run on GitHub-hosted machines, so WSL and administrator access on your computer are not required.

---

## 📝 License & Credits

This project was created by **Redcat 607** and is protected under the [GNU GPLv3 License](LICENSE).

You are completely free to use, modify, and distribute this software! However, under the GPLv3 terms,
**you must give appropriate credit**, keep the original copyright notice intact, 
and any modified versions you share must also be open-source under the exact same license. 🐾✨