import customtkinter as ctk
from config import APP_NAME, WINDOW_SIZE
from gui.styles import theme

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Basic window config
        self.title(APP_NAME)
        self.geometry(WINDOW_SIZE)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        #Apply theme
        self.configure(bg=theme["bg_color"])

        # Title label
        self.title_label = ctk.CTkLabel(self, text="🔐 Text Encryption & Decryption App", font=theme["font_bold"], text_color=theme["fg_color"])
        self.title_label.pack(pady=(20, 10))

        # Password input
        self.password_box = ctk.CTkEntry(self, placeholder_text="Enter password", show="*", width=300)
        self.password_box.pack(pady=10)

        # Text input
        self.input_box = ctk.CTkEntry(self, placeholder_text="Enter your message here...", width=300)
        self.input_box.pack(pady=10)

        # Encrypt & Decrypt buttons
        self.encrypt_btn = ctk.CTkButton(self, text="Encrypt", command=self.encrypt_dummy)
        self.encrypt_btn.pack(pady=5)

        self.decrypt_btn = ctk.CTkButton(self, text="Decrypt", command=self.decrypt_dummy)
        self.decrypt_btn.pack(pady=5)

        # Output area
        self.output_box = ctk.CTkTextbox(self, width=300, height=100)
        self.output_box.pack(pady=(10, 20))

    def encrypt_dummy(self):

        self.output_box.delete("1.0", "end")

        password = self.password_box.get()
        if not password:
           self.output_box.insert("end", "⚠️ Please Enter a Password.")
           return
        
        self.output_box.insert("end", "🔒 Encrypted output will appear here")

    def decrypt_dummy(self):
        self.output_box.delete("1.0", "end")

        password = self.password_box.get()
        if not password:
           self.output_box.insert("end", "⚠️ Please enter a password.")
           return 
               
        self.output_box.insert("end", "🔓 Decrypted text will appear here")
