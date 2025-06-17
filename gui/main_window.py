import customtkinter as ctk
from backend.encryption import encrypt_message, decrypt_message
from gui.styles import theme
import tkinter.filedialog as fd
from backend.storage import save_to_file, load_from_file
from config import APP_NAME, MASTER_PASSWORD
import pyperclip

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Basic window config
        self.title(APP_NAME)

        # Size and center
        window_width = 600
        window_height = 480
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.configure(bg=theme["bg_color"])

        # Title label
        self.title_label = ctk.CTkLabel(
            self, text="🔐 Text Encryptor & Decryptor",
            font=theme["font_bold"], text_color=theme["fg_color"]
        )
        self.title_label.pack(pady=(20, 10))

        # Password input
        self.password_box = ctk.CTkEntry(
            self, placeholder_text="Enter master password", show="*", width=400
        )
        self.password_box.pack(pady=10)

        # Text input
        self.input_box = ctk.CTkEntry(
            self, placeholder_text="Enter your message here...", width=400
        )
        self.input_box.pack(pady=10)

        # Encrypt & Decrypt buttons side by side
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        self.encrypt_btn = ctk.CTkButton(button_frame, text="🔐 Encrypt", command=self.encrypt_dummy, width=180)
        self.encrypt_btn.grid(row=0, column=0, padx=10)

        self.decrypt_btn = ctk.CTkButton(button_frame, text="🔓 Decrypt", command=self.decrypt_dummy, width=180)
        self.decrypt_btn.grid(row=0, column=1, padx=10)

        # Output box
        self.output_box = ctk.CTkTextbox(self, width=500, height=100)
        self.output_box.pack(pady=10)

        # Copy & Clear buttons side by side
        utility_frame = ctk.CTkFrame(self, fg_color="transparent")
        utility_frame.pack(pady=5)

        self.copy_btn = ctk.CTkButton(utility_frame, text="📋 Copy Output", command=self.copy_output, width=180)
        self.copy_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = ctk.CTkButton(utility_frame, text="🧹 Clear", command=self.clear_fields, width=180)
        self.clear_btn.grid(row=0, column=1, padx=10)

        # Save & Load buttons side by side
        file_frame = ctk.CTkFrame(self, fg_color="transparent")
        file_frame.pack(pady=10)

        self.save_btn = ctk.CTkButton(file_frame, text="💾 Save to File", command=self.save_to_file, width=180)
        self.save_btn.grid(row=0, column=0, padx=10)

        self.load_btn = ctk.CTkButton(file_frame, text="📂 Load from File", command=self.load_from_file, width=180)
        self.load_btn.grid(row=0, column=1, padx=10)


    def encrypt_dummy(self):
        self.output_box.delete("1.0", "end")

        password = self.password_box.get()
        if password != MASTER_PASSWORD:
            self.output_box.insert("end", "❌ Incorrect password! Access denied.")
            return

        message = self.input_box.get()
        if not message:
            self.output_box.insert("end", "⚠️ Please enter a message to encrypt.")
            return

        encrypted_text, salt = encrypt_message(message, password)

        # Combine encrypted text and salt so it can be decrypted later
        result = f"{encrypted_text}:::{salt}"
        self.output_box.insert("end", result)


    def decrypt_dummy(self):
        self.output_box.delete("1.0", "end")

        password = self.password_box.get()
        if password != MASTER_PASSWORD:
            self.output_box.insert("end", "❌ Incorrect password! Access denied.")
            return

        encrypted_combo = self.input_box.get()
        if not encrypted_combo:
            self.output_box.insert("end", "⚠️ Please enter encrypted text to decrypt.")
            return

        try:
            encrypted_text, salt = encrypted_combo.split(":::")
        except ValueError:
            self.output_box.insert("end", "⚠️ Invalid encrypted format.")
            return

        decrypted = decrypt_message(encrypted_text, password, salt)

        if decrypted is None:
            self.output_box.insert("end", "❌ Wrong password or corrupted data.")
        else:
            self.output_box.insert("end", decrypted)


    def save_to_file(self):
        data = self.output_box.get("1.0", "end").strip()
        if not data:
            self.output_box.insert("end", "\n⚠️ Nothing to save.")
            return

        file_path = fd.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
        if file_path:
            success = save_to_file(file_path, data)
            if success:
                self.output_box.insert("end", f"\n✅ Saved to {file_path}")
            else:
                self.output_box.insert("end", "\n❌ Failed to save file.")

    def load_from_file(self):
        file_path = fd.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
        if file_path:
            content = load_from_file(file_path)
            if content:
                self.input_box.delete(0, "end")
                self.input_box.insert(0, content)
                self.output_box.insert("end", f"\n✅ Loaded from {file_path}")
            else:
                self.output_box.insert("end", "\n❌ Failed to load file.")

    def copy_output(self):
        output = self.output_box.get("1.0", "end").strip()
        if output:
            pyperclip.copy(output)
            self.output_box.insert("end", "\n✅ Output copied to clipboard.")

    def clear_fields(self):
        self.output_box.delete("1.0", "end")
        self.input_box.delete(0, "end")        