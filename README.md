# 🔐 Text Encryption & Decryption App

A professional desktop application built with **Python** and **CustomTkinter** for secure text encryption and decryption. It features password-protected encryption, powered by the **cryptography library**, ensuring that only users with the master password can decrypt the data. The app includes a clean, modern GUI and supports saving and loading encrypted text files.

---

## ✨ Features:

* 🔑 **Password-based encryption and decryption** only work with the correct master password.
* 📋 **Copy output** easily to clipboard.
* 💾 **Save and load encrypted messages** from files with intuitive dialogs.
* 🧹 **Clear inputs and outputs** instantly.
* 🖥️ **Modern GUI** built with CustomTkinter, featuring dark mode and green accent theme.
* 🎯 **Centered fixed-size window** for consistent UX.

---

## 🧰 Tech Stack:
The following tech stack is used in this project:


| Purpose                       | Technology                                     |
| ----------------------------- | ---------------------------------------------- |
| Programming Language          | Python 3.x                                     |
| GUI Framework                 | CustomTkinter (modern, customizable UI)        |
| Encryption/Decryption Library | Cryptography (secure symmetric encryption)     |
| System Theme Detection        | Darkdetect (auto dark/light mode)              |
| Clipboard Support             | Pyperclip (copy/paste functionality)           |
| Build Tools                   | Cffi, pycparser (C extensions for performance) |

---

## 📂 Project Structure:
This is the complete project structure used to develop this application:

```
text-encryption-decryption-app/
│
├── backend/
│   ├── encryption.py     # Encryption and decryption logic
│   └── storage.py        # File save/load utilities
├── gui/
│   ├── main_window.py    # GUI layout and event handling
│   └── styles.py         # Custom styles and themes
├── venv/                 # Python environment and installed libraries.
├── .gitignore            # Skip unwanted files in Git
├── app.py                # Main GUI application file
├── config.py             # Master password and configurations
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## ⚙️ How to Run the Project:
Follow these steps to successfully run the project:

#### 1. **Clone the repository:**

```bash
https://github.com/PAIshanMadusha/text-encryption-decryption-app.git
cd text-encryption-decryption-app
```

#### 2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/macOS
```

#### 3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

#### 4. Usage & **Run the app:**

```bash
python app.py
```

* 🔐 Enter the **master password** (found in `config.py` as `MASTER_PASSWORD = "PAIshanMadusha"`).
* ✍️ Input your **message** to encrypt or decrypt.
* 🔒 Click **Encrypt** or **Decrypt** to perform operations.
* 📋 Use **Copy Output** to copy results.
* 💾 Save or load encrypted text files using **Save to File** / **Load from File**.
* 🧹 Click **Clear** to reset fields.

---

## ⚙️ How It Works:

* Uses your **master password** to generate a secure key for **symmetric encryption** via the `cryptography` library.
* Encrypts text input and displays the result instantly in the app.
* Decryption only works with the correct master password.
* Supports saving encrypted text to files and loading it back securely.
* All encryption and decryption are handled **locally** for maximum privacy.

## 📸 System Screenshots:

---
<p align="center">
  <img src="https://github.com/user-attachments/assets/3a91757f-1d95-4329-ae68-06d7fcf94df8" alt="Screenshot 1" width="350">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/9f157fb2-38d8-4c5d-a981-4d437202287a" alt="Screenshot 3" width="350">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <br><br>
  <img src="https://github.com/user-attachments/assets/1268aafb-c6ed-4ad6-add4-0f085c011c5c" alt="Screenshot 4" width="350">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/48b468ec-2d98-496a-a6eb-2c84963b4b09" alt="Screenshot 4" width="350">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

---

### 👨‍💻 Created by: 
**Ishan Madhusha**  
GitHub: [PAIshanMadusha](https://github.com/PAIshanMadusha)

Feel free to explore my work and get in touch if you'd like to collaborate! 🚀

---

## 📝 License:  
This project is licensed under the MIT License : See the [LICENSE](LICENSE) file for details.
